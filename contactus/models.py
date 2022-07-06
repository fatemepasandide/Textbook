from django.db import models
from django.utils import timezone

class ContactUs (models.Model):
    email_contact   = models.EmailField(max_length=30,null=True)
    name            = models.CharField(max_length=40)
    phone_number    = models.CharField(max_length=12)
    subject         = models.CharField(max_length=30,null=True)
    message_contact = models.TextField(max_length=300,null=True)
    created_at      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
