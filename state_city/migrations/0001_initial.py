# Generated by Django 3.2 on 2021-05-10 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30)),
                ('state_id', models.ForeignKey(db_column='state_id', on_delete=django.db.models.deletion.CASCADE, to='state_city.states')),
            ],
            options={
                'db_table': 'cities',
            },
        ),
    ]
