# Generated by Django 4.1.4 on 2023-01-07 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0016_alter_quote_date_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ['-created']},
        ),
    ]
