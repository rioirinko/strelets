# Generated by Django 2.2.10 on 2020-04-06 15:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Number in format: +996555111222', regex='^[+996][0-9]{12,12}$')], verbose_name='Телефон')),
                ('passport', models.CharField(max_length=50, verbose_name='Паспорт')),
                ('position', models.IntegerField(choices=[(1, 'АДМИНИСТРАТОР'), (2, 'БАРМЕН'), (3, 'ГОРНИЧНАЯ')], default=1, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('comment', models.CharField(max_length=500, verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('type_of_number', models.CharField(max_length=100, verbose_name='Тип номера')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Number in format: +996555111222', regex='^[+996][0-9]{12,12}$')], verbose_name='Номер телефона')),
                ('mail', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('service', models.IntegerField(choices=[(1, 'Да'), (2, 'Нет')], default=1, verbose_name='Трансфер с аэропорта')),
                ('arrival_date', models.DateField(verbose_name='Дата въезда')),
                ('date_of_departure', models.DateField(verbose_name='Дата выезда')),
                ('payment', models.IntegerField(choices=[(1, 'Наличные'), (2, 'Онлайн')], default=1, verbose_name='Способ оплаты')),
                ('price', models.CharField(max_length=250, verbose_name='Цена за номер')),
                ('comment', models.CharField(max_length=250, verbose_name='Комментарии')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='hotel.Room', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
            },
        ),
    ]
