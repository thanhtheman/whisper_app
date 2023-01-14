# Generated by Django 4.1.4 on 2023-01-14 02:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_consent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='consent',
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')])),
                ('consent', models.BooleanField(blank=True, null=True)),
                ('phone_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
    ]