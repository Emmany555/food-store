# Generated by Django 4.1a1 on 2022-08-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_seller_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller_contact',
            field=models.CharField(max_length=25),
        ),
    ]
