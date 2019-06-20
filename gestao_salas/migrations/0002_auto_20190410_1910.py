# Generated by Django 2.1.5 on 2019-04-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_salas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentals',
            name='data_final',
            field=models.CharField(choices=[('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00')], max_length=6),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='data_inicio',
            field=models.CharField(choices=[('00:00', '00:00'), ('00:30', '00:30'), ('01:00', '01:00'), ('01:30', '01:30'), ('02:00', '02:00'), ('02:30', '02:30'), ('03:00', '03:00'), ('03:30', '03:30'), ('04:00', '04:00'), ('04:30', '04:30'), ('05:00', '05:00')], max_length=6),
        ),
    ]
