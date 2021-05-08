from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


# Create your models here.


class AdvUser(AbstractUser):
    send_message = models.BooleanField(default=True, verbose_name='Слать оповещеие о новых комментария')

    class Meta(AbstractUser.Meta):
        pass

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #     super().save(*args, **kwargs)
