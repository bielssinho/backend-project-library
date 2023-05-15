from django.db import models
import uuid

class Copy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    book = models.ForeignKey(
        "books.Book",
        related_name="copy",
        on_delete=models.CASCADE
    )
