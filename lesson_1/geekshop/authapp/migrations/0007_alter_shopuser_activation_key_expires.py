# Generated by Django 3.2.7 on 2021-11-13 10:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20211113_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 15, 10, 13, 54, 456209, tzinfo=utc)),
        ),
    ]
