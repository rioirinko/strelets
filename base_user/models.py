import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Невозможно создать пользователя без электронной почты")

        if not password:
            raise ValueError("Невозможно создать пользователя без пароля")

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


GENDER_CHOICES = (
    (1, 'Женский'),
    (2, 'Мужской'),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name='Пол')
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False,
        verbose_name='E-mail'
        )
    birthday = models.DateField(verbose_name='День рождение')
    country = models.CharField(max_length=250, verbose_name='Страна проживания')
    passport = models.CharField(max_length=250, verbose_name='Номер паспорта')
    points = models.IntegerField(verbose_name='Баллы')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')

    class Meta:
        app_label = 'base_user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'