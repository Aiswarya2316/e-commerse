# Generated by Django 5.0.7 on 2024-08-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_delpro_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='del_boy',
            field=models.BooleanField(default=True),
        ),
    ]