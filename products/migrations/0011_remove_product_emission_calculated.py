# Generated by Django 4.1.3 on 2022-11-19 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_emission_calculated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='emission_calculated',
        ),
    ]
