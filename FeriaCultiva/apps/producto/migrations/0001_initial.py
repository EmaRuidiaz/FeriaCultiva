# Generated by Django 2.2.6 on 2019-10-21 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feriante', '0001_initial'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField()),
                ('foto_producto', models.ImageField(null=True, upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productosXcategoria', to='categoria.Categoria')),
                ('feriante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productosXferiante', to='feriante.Feriante')),
            ],
        ),
    ]
