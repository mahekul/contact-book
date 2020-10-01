from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField()
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
