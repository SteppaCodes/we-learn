from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
import uuid
from .managers import CustomuserManager


class User(AbstractBaseUser, PermissionsMixin):
    id =models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField(_('Email Address'), unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomuserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    @property
    def fullname(self):
        return f"{self.last_name} {self.first_name}"


