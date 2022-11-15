from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):

    def _create_user(self, email, password, team, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, team=team, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, team='MANAGEMENT', **extra_fields)


class User(AbstractUser):

    TEAM = [('SALES', 'SALES'),
            ('SUPPORT', 'SUPPORT'),
            ('MANAGEMENT', 'MANAGEMENT')]

    # Disable username field and enable login via email
    username = None
    email = models.EmailField(unique=True)
    team = models.fields.CharField(max_length=10, choices=TEAM,
                                   blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['team']

    objects = CustomUserManager()