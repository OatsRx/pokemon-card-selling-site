# Generated by Django 3.1.2 on 2020-10-17 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_friendly_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]