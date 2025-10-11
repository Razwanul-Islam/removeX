import random
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from uuid import uuid4


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150,null=True,blank=True)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    phone = models.CharField(max_length=50,null=True,blank=True)
    is_verified = models.BooleanField(default=False)
    attributes = models.JSONField(default=dict, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        unique_together = ['email', "username"]
        db_table = 'auth_user' 