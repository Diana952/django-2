# Generated by Django 3.2.16 on 2022-11-01 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_user_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patronymic',
            field=models.CharField(blank=True, max_length=200, verbose_name='Отчество'),
        ),
    ]