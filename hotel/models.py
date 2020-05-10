from django.contrib.auth import get_user_model
from django.db import models
from hotel.validators import validate_number
from django.core import validators

User = get_user_model()

YESNO_CHOICES = (
    (1, 'Да'),
    (2, 'Нет'),
)


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    number_of_beds = models.IntegerField(verbose_name='Количество кроватей')
    family_apartment = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Семейный номер')
    bathroom = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Ванная')
    number_of_places = models.CharField(max_length=250, verbose_name='Размер номера')
    mini_bar = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Мини бар')
    tv = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Телевизор')
    air_conditioning = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Кондиционер')
    wi_fi = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Wi-Fi')
    refrigerator = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Холодильник')
    pets = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Можно с питомцами')
    price = models.IntegerField(verbose_name='Стоимость')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', max_length=500, null=True, blank=True, verbose_name='Фото')
    free = models.BooleanField(default=True, verbose_name='Свободный')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'


EMPLOYEE_CHOICES = (
    (1, 'АДМИНИСТРАТОР'),
    (2, 'БАРМЕН'),
    (3, 'ГОРНИЧНАЯ'),
)


class Employee(models.Model):
    name = models.CharField(max_length=300, verbose_name='ФИО')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    phone = models.CharField(validators=validate_number(), max_length=13, verbose_name='Телефон')
    passport = models.CharField(max_length=50, verbose_name='Паспорт')
    position = models.IntegerField(choices=EMPLOYEE_CHOICES, default=1, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Services(models.Model):
    description = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Questions(models.Model):
    name = models.CharField(max_length=250, verbose_name='ФИО')
    mail = models.EmailField(validators=[validators.validate_email], blank=False, verbose_name='E-mail')
    message_subject = models.CharField(max_length=100, verbose_name='Тема сообщения')
    question = models.CharField(max_length=1000, verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Пользователь', null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name='ФИО')
    number = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE, verbose_name='Номер')
    phone = models.CharField(validators=validate_number(), max_length=13, verbose_name='Номер телефона')
    passport = models.CharField(max_length=50, verbose_name='Паспорт')
    mail = models.EmailField(validators=[validators.validate_email], blank=False, verbose_name='E-mail')
    service = models.IntegerField(choices=YESNO_CHOICES, default=1, verbose_name='Трансфер с аэропорта')
    arrival_date = models.DateField(verbose_name='Дата въезда')
    date_of_departure = models.DateField(verbose_name='Дата выезда')
    price = models.IntegerField(null=True, verbose_name='Цена за номер')
    comment = models.CharField(max_length=250, verbose_name='Комментарии')
    reservation = models.BooleanField(default=False, verbose_name='Подтвердить бронь')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'


class Review(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    comment = models.CharField(max_length=500, verbose_name='Отзыв')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
