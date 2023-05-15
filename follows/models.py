from django.db import models
import uuid

class Follow(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="followers_user"
    )
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="followers_books"
    )
