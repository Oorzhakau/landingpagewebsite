# Generated by Django 4.0 on 2021-12-18 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricecart',
            options={'verbose_name': 'Цены', 'verbose_name_plural': 'Цены'},
        ),
        migrations.AlterModelOptions(
            name='pricetable',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
    ]