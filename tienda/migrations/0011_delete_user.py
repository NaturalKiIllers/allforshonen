# Generated by Django 3.1.1 on 2020-11-01 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]