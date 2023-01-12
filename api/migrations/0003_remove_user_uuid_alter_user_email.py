# Generated by Django 4.1.5 on 2023-01-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
