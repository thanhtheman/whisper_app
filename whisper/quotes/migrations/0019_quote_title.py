# Generated by Django 4.1.4 on 2023-01-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0018_alter_quote_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]