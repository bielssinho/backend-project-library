from django.urls import path
from . import views
from .views import CopyView

urlpatterns = [
    path("copys/", views.CopyView.as_view()),
]
