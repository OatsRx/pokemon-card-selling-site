# Generated by Django 3.1.2 on 2020-10-26 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201020_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rarity',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]