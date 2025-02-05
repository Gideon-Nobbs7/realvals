import uuid
from django.db import models
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(default="myval@gmail.com")
    phone_number = models.CharField(max_length=20, default="0247965219")
    message_to_lover = models.TextField(default="Hey [lover], I have...")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.id}"
