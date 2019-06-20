# Generated by Django 2.1.2 on 2019-06-19 23:03

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190620_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telemovel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]