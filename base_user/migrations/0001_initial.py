# Generated by Django 2.2.10 on 2020-05-07 18:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='ФИО')),
                ('gender', models.IntegerField(choices=[(1, 'Женский'), (2, 'Мужской')], default=1, verbose_name='Пол')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail')),
                ('birthday', models.DateField(verbose_name='День рождение')),
                ('country', models.CharField(max_length=250, verbose_name='Страна проживания')),
                ('passport', models.CharField(max_length=250, verbose_name='Номер паспорта')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]