# Generated by Django 4.1a1 on 2022-08-30 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_product_seller_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(blank=True, default='', upload_to='profile_images'),
        ),
    ]
