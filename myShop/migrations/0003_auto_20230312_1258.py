# Generated by Django 3.2.17 on 2023-03-12 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myShop', '0002_alter_product_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothescategory',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='clothescategory',
            name='unit',
        ),
    ]