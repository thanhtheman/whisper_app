# Generated by Django 4.1.4 on 2023-01-14 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_profile_consent_alter_profile_phone_number_and_more'),
        ('quotes', '0017_alter_quote_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
