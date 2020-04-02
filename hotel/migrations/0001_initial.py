# Generated by Django 3.0.5 on 2020-04-02 15:43

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
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('number_of_places', models.IntegerField(verbose_name='Кол-во мест')),
                ('type_of_number', models.IntegerField(choices=[(1, 'СТАНДАРТНЫЙ'), (2, 'ЭКОНОМ'), (3, 'ПОЛУЛЮКС'), (4, 'ЛЮКС')], default=1, verbose_name='Тип номера')),
                ('price', models.IntegerField(verbose_name='Стоимость')),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='media/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='ФИО')),
                ('passport', models.CharField(max_length=50, verbose_name='Паспорт')),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Number in format: +996555111222', regex='^[+996][0-9]{12,12}$')], verbose_name='Телефон')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('arrival_date', models.DateField(verbose_name='Дата въезда')),
                ('date_of_departure', models.DateField(verbose_name='Дата выезда')),
                ('total_sum', models.CharField(max_length=50, verbose_name='Оплата')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='population_data', to='hotel.Employee', verbose_name='Сотрудник')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='hotel.Room', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleaning', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cla', to='hotel.Employee')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cle', to='hotel.Room')),
            ],
            options={
                'verbose_name': 'Уборка',
                'verbose_name_plural': 'Уборка',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Number in format: +996555111222', regex='^[+996][0-9]{12,12}$')], verbose_name='Телефон')),
                ('arrival_date', models.DateField(verbose_name='Дата въезда')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='hotel.Room')),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирование',
            },
        ),
    ]
