from django.db import models
from hotel.validators import validate_number

STATUS_CHOICES = (
    (1, 'СТАНДАРТНЫЙ'),
    (2, 'ЭКОНОМ'),
    (3, 'ПОЛУЛЮКС'),
    (4, 'ЛЮКС'),
)


class Room(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    number_of_places = models.IntegerField(verbose_name='Кол-во мест')
    type_of_number = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Тип номера')
    price = models.IntegerField(verbose_name='Стоимость')
    image = models.ImageField(upload_to='media/', max_length=500, null=True, blank=True, verbose_name='Фото')

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


class Customer(models.Model):
    name = models.CharField(max_length=300, verbose_name='ФИО')
    passport = models.CharField(max_length=50, verbose_name='Паспорт')
    phone = models.CharField(validators=validate_number(), max_length=13, verbose_name='Телефон')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    number = models.ForeignKey(Room, related_name='customer', on_delete=models.CASCADE, verbose_name='Номер')
    employee = models.ForeignKey(Employee, related_name='population_data', on_delete=models.CASCADE,
                                 verbose_name='Сотрудник')
    arrival_date = models.DateField(verbose_name='Дата въезда')
    date_of_departure = models.DateField(verbose_name='Дата выезда')
    total_sum = models.CharField(max_length=50, verbose_name='Оплата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Cleaning(models.Model):
    number = models.ForeignKey(Room, related_name='cle', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='cla', on_delete=models.CASCADE)
    cleaning = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Уборка'
        verbose_name_plural = 'Уборка'


class Booking(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(validators=validate_number(), max_length=13, verbose_name='Телефон')
    number = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE)
    arrival_date = models.DateField(verbose_name='Дата въезда')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
