from django.urls import path
from . import views

urlpatterns = [
    path("loans/", views.LoansView.as_view()),
    path("loans/<uuid:pk>/", views.LoansAdminView.as_view()),
    path("loans/user/<uuid:pk>/", views.LoansUserView.as_view())

]