from django.contrib.auth.models import User
from django.db import models
import uuid

class Morador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apartamento = models.CharField(max_length=10)
    token_qr = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return f"{self.user.username} - Apto {self.apartamento}"