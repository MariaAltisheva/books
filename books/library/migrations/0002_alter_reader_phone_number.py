# Generated by Django 4.1.7 on 2023-03-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='phone_number',
            field=models.CharField(max_length=11, null=7, verbose_name='телефон читателя'),
        ),
    ]
