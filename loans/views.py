from django.shortcuts import get_object_or_404
from books.permission import IsAdminOrReadOnly
from loans.exceptions import alreadyBorrowed, alreadyDevoluted, blockedUser
from loans.permissions import IsAdminOrLoanOwner
from .models import Loan
from copys.models import Copy
from .serializers import LoansSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import datetime, timedelta

class LoansView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    queryset = Loan.objects.all()
    serializer_class = LoansSerializer


class LoansAdminView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    queryset = Loan.objects.all()
    serializer_class = LoansSerializer
    
    def perform_update(self, serializer):
        loan = get_object_or_404(Loan, pk=self.kwargs["pk"])
        if not loan.borrowed_date:
            borrowed_date = datetime.today()
            devolution_date = borrowed_date + timedelta(days=7)

            while devolution_date.weekday() >= 5:
                devolution_date += timedelta(days=1)

            serializer.save(borrowed_date=borrowed_date, devolution_date=devolution_date)
        else:
            raise alreadyBorrowed


class LoansUserView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrLoanOwner]

    queryset = Loan.objects.all()
    serializer_class = LoansSerializer

    def perform_create(self, serializer) -> None:
        copy = get_object_or_404(Copy, pk=self.kwargs["pk"])
        user = self.request.user

        if self.queryset.filter(copy=copy, is_devoluted=False):
            raise alreadyBorrowed
        
        for borrowed in user.historic.all():
            today = datetime.today().date()
            if (
                not borrowed.is_devoluted
                and borrowed.devolution_date
                and today > borrowed.devolution_date.date()
            ) or (borrowed.blocked_until and today < borrowed.blocked_until.date()):
                user.can_borrow = False
                user.save()
            else:
                user.can_borrow = True
                user.save()

        if user.can_borrow:
            serializer.save(copy=copy, user=user)
        else:
            raise blockedUser

    def perform_update(self, serializer):
        loan = get_object_or_404(Loan, pk=self.kwargs["pk"])
        today = datetime.today()

        if (not loan.is_devoluted and today.date() > loan.devolution_date.date()):
            serializer.save(is_devoluted=True, blocked_until = today + timedelta(days=3))
        elif(not loan.is_devoluted):
            serializer.save(is_devoluted=True)
        else:
            raise alreadyDevoluted
        
        