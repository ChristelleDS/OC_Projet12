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

    def create_user(self, email, password=None, team=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, team, **extra_fields)

    def create_superuser(self, email, password=None, team='MANAGEMENT', **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, team='MANAGEMENT', **extra_fields)


class User(AbstractUser):

    # Disable username field and enable login via email
    username = None
    email = models.EmailField(unique=True)

    # Groups to manage edition authorizations
    TEAM = [('SALES', 'SALES'),
            ('SUPPORT', 'SUPPORT'),
            ('MANAGEMENT', 'MANAGEMENT')]
    team = models.fields.CharField(max_length=10, choices=TEAM,
                                   blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['team']

    # Make a new member active & staff by default, so it can do CRUD operations
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = CustomUserManager()
