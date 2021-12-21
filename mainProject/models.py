from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SubProject(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  workingOn = models.CharField(max_length=100)
  mainProjectnum = models.CharField(max_length=10)
  
  
class MainProject(models.Model):
  title = models.CharField(max_length=200)
  type = models.CharField(max_length=200)
  
  
# class User(AbstractUser):
#    username = None
#     email = models.EmailField(_('email address'), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []