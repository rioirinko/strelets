from django.db import models
from hotel.validators import validate_number


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Номер')
    price = models.IntegerField(verbose_name='Стоимость')
    description = models.CharField(max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='media/', max_length=500, null=True, blank=True, verbose_name='Фото')
    number_of_places = models.CharField(max_length=250, verbose_name='Количество мест')
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


# class Customer(models.Model):
#     name = models.CharField(max_length=300, verbose_name='ФИО')
#     passport = models.CharField(max_length=50, verbose_name='Паспорт')
#     phone = models.CharField(validators=validate_number(), max_length=13, verbose_name='Телефон')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Клиент'
#         verbose_name_plural = 'Клиенты'


class Services(models.Model):
    description = models.CharField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


BOOKING_CHOICES = (
    (1, 'Да'),
    (2, 'Нет'),
)

PAYMENT_CHOICES = (
    (1, 'Наличные'),
    (2, 'Онлайн'),
)


class Booking(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    number = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE, verbose_name='Номер')
    phone = models.CharField(validators=validate_number(), max_length=13, verbose_name='Номер телефона')
    mail = models.EmailField(max_length=254, verbose_name='E-mail')
    service = models.IntegerField(choices=BOOKING_CHOICES, default=1, verbose_name='Трансфер с аэропорта')
    arrival_date = models.DateField(verbose_name='Дата въезда')
    date_of_departure = models.DateField(verbose_name='Дата выезда')
    payment = models.IntegerField(choices=PAYMENT_CHOICES, default=1, verbose_name='Способ оплаты')
    price = models.IntegerField(null=True, verbose_name='Цена за номер')
    comment = models.CharField(max_length=250, verbose_name='Комментарии')

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
