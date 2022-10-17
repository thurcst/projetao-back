from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import copy

# Modelo de usuário
class User(AbstractUser):
    # Elementos da tabela, de acordo com o modelo
    nick = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(("email address"), unique=True)
    username = copy.deepcopy(nick)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    class Meta:  ## Nome da tabela no MariaDB

        db_table = "user_profile"

    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
