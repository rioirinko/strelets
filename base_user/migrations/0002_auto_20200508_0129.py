# Generated by Django 2.2.10 on 2020-05-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=255, verbose_name='ФИО'),
        ),
    ]