from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    
    SEX_CHOICES = (
        ('M' , 'Male'),
        ('F', 'Female')
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)