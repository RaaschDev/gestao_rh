# Generated by Django 4.0.2 on 2022-02-21 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='nome',
            field=models.CharField(help_text='Nome do funcionario', max_length=100, verbose_name='Nome'),
        ),
    ]
