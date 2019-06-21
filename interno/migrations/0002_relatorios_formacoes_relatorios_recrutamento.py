# Generated by Django 2.1.2 on 2019-06-20 22:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interno', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relatorios_formacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Relatorios_recrutamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(verbose_name=2019)),
                ('semestre', models.CharField(choices=[('1º Semestre', '1º Semestre'), ('2º Semestre', '2º Semestre')], max_length=10)),
                ('n_vagas_tec', models.IntegerField(default=0)),
                ('n_vagas_ino', models.IntegerField(default=0)),
                ('n_vagas_int', models.IntegerField(default=0)),
                ('n_candidatos', models.IntegerField(default=0)),
                ('n_grupos', models.IntegerField(default=0)),
                ('n_min_grupo', models.IntegerField(default=0)),
                ('n_max_grupo', models.IntegerField(default=0)),
                ('n_individual', models.IntegerField(default=0)),
                ('n_estagio', models.IntegerField(default=0)),
                ('n_admitidos', models.IntegerField(default=0)),
                ('responsavel', models.ManyToManyField(related_name='responsavel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]