from django.urls import path
from . import views
from .views import FollowView

urlpatterns = [
    path("follow/<uuid:pk>/", views.FollowView.as_view()),
]
