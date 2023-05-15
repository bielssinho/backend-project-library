from django.db import models
import uuid 

class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=50)
    category = models.CharField()
    realese_date = models.DateField()
    synopsis = models.TextField()
    author = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
