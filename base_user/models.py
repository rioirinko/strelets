import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser

from base_user.managers import BaseUserManager

GENDER_CHOICES = (
    (1, 'Женский'),
    (2, 'Мужской'),
)


class BaseUser(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='ФИО')
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1, verbose_name='Пол')
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False,
        verbose_name='E-mail'
        )
    birthday = models.DateField(verbose_name='День рождение', null=True, blank=True)
    country = models.CharField(max_length=250, verbose_name='Страна проживания')
    passport = models.CharField(max_length=250, verbose_name='Номер паспорта')
    points = models.IntegerField(verbose_name='Баллы', null=True, blank=True, default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = BaseUserManager()

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