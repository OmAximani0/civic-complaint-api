# Generated by Django 3.2 on 2021-09-28 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_adhar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='city_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='users',
            name='state_id',
            field=models.CharField(max_length=100),
        ),
    ]
