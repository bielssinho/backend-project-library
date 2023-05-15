from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True, max_length=150)
    password = models.CharField(max_length=150)
    is_employe = models.BooleanField(default=False)
    can_borrow = models.BooleanField(default=True)

    follows = models.ManyToManyField(
        "users.User",
        through="follows.Follow",
        related_name="follow_user",
    )

    copys = models.ManyToManyField(
        "copys.Copy",
        through="loans.Loan",
        related_name="users_copys",
    )