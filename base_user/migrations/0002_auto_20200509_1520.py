# Generated by Django 2.2.10 on 2020-05-09 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseuser',
            name='points',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Баллы'),
        ),
    ]
