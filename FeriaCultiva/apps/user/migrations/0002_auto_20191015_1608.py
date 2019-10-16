# Generated by Django 2.2.6 on 2019-10-15 19:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(default='Carlos Boggio 1234', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='es_empresa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='foto_perfil',
            field=models.ImageField(null=True, upload_to='cliente'),
        ),
        migrations.AddField(
            model_name='user',
            name='telefono',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed', regex='\\+?1?\\d(9,15)$')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Ya existe un usuario con este email.'}, max_length=254, unique=True, verbose_name='direccion de correo'),
        ),
    ]