from django.db import models
import uuid 

class Loan(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    borrowed_date  = models.DateTimeField(null=True)
    devolution_date  = models.DateTimeField(null=True)
    is_devoluted = models.BooleanField(null=True, default=False)
    blocked_until = models.DateTimeField(null=True)

    copy = models.ForeignKey(
        "copys.Copy",
        on_delete=models.CASCADE,
        related_name="loans_copys",
    )

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="historic",
    )

    def __repr__(self) -> str:
        return f"<Loans {self.id}>"
