# Generated by Django 4.2.2 on 2024-11-28 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0006_alter_language_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_details',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact_details',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact_details',
            name='mobile',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact_details',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact_details',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.supplier'),
        ),
        migrations.AlterField(
            model_name='contact_details',
            name='whatsapp',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]