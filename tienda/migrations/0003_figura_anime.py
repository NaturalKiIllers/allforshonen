# Generated by Django 3.1.1 on 2020-10-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_figura_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='figura',
            name='anime',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
