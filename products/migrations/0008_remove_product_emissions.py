# Generated by Django 4.1.3 on 2022-11-19 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_emissions_alter_product_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='emissions',
        ),
    ]
