# Generated by Django 3.2.7 on 2021-09-28 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postre',
            name='image',
            field=models.ImageField(upload_to='Postre'),
        ),
    ]
