# Generated by Django 4.2.2 on 2024-12-20 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0014_guide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('reminder_id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]