# Generated by Django 4.1.3 on 2022-12-26 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_quote_date_quote_time_delete_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='scheduling_time',
        ),
    ]