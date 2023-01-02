# Generated by Django 4.1.4 on 2023-01-02 12:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0013_remove_quote_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='time',
            new_name='date_time',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='date',
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('time_tag', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('quote_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quotes.quote')),
            ],
        ),
    ]
