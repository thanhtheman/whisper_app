# Generated by Django 4.1.4 on 2023-01-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_profile_img.svg', null=True, upload_to='images/'),
        ),
    ]
