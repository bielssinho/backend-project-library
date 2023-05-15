from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Follow
from .serializer import FollowsSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
from books.models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class FollowView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Follow.objects.all()
    serializer_class = FollowsSerializer
    lookup_url_kwarg = "pk"

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(book=book, user=self.request.user)
        email = self.request.user.email
        message = f"Você seguiu o livro {book.title}"

        send_mail(
            "Library Follow",
            message,
            settings.EMAIL_HOST,
            [email],
        )
