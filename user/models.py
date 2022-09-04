"""
Custom models for user and user manager
Token generation along with User instance creation using django signals
"""

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Custom UserManager to create user and superuser"""

    def create_user(self,email=None,name=None,password=None,**extra_fields):
        """create, save and return a new user"""

        if not email:
            raise ValueError(_("Please enter a valid Email ID!"))
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email),name=name,**extra_fields)
        user.is_superuser = False
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self,email=None,name=None,password=None):
        """create, save and return a new super user with is_superuser=True"""

        user = self.create_user(email=email, name=name, password=password)
        user.is_superuser = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser,PermissionsMixin):
    """Custom user in system, attrubutes ->email(username), name, password, is_superuser """

    email = models.EmailField(_("Email Address"),unique=True)
    name = models.CharField(_("Name"),max_length=32,blank=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self) -> str:
        """ string displayed in place of user object """
        return f"{self.email}"
  

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """ Creating auth token once user model is created using django signals"""
    if created:
        Token.objects.create(user=instance)
