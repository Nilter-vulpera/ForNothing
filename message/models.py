from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


# Create your models here.
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


# Create your models here.
class Mes(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='send_messages')
    addressee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='taken_messages')
    time_create = models.DateTimeField(default=timezone.now)
    content = models.TextField()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='', blank=True)
    time_create = models.DateTimeField(default=timezone.now)
