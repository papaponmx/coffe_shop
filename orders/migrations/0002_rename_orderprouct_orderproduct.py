# Generated by Django 5.1.1 on 2024-09-29 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('products', '0002_alter_product_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderProuct',
            new_name='OrderProduct',
        ),
    ]
