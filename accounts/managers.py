from django.contrib.auth.base_user import BaseUserManager
from  django.utils.translation import gettext_lazy as _ 


class CustomUserManager(BaseUserManager):
    """
    This is a custom modelmanager where email is the unique identifiers for authentication and not username
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('email is a required field'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        create and save a superuser with a given emaila and password
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser=True'))
        return self.create_user(email, password, **extra_fields)
