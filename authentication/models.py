from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.contrib.auth.hashers import make_password


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    TEAM = [('SALES', 'SALES'),
            ('SUPPORT', 'SUPPORT'),
            ('MANAGEMENT', 'MANAGEMENT'),
            ('CONSULT', 'CONSULT')]

    # Disable username field and enable login via email
    username = None
    email = models.EmailField(unique=True)
    team = models.fields.CharField(max_length=10, choices=TEAM,
                                   blank=False, default='CONSULT')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Make a new member active & staff by default, so it can do CRUD operations
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=True)
    objects = CustomUserManager()
