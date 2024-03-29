# Generated by Django 2.1.1 on 2020-07-17 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ciudad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=70)),
                ('direccion', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('active', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ciudad.Ciudad')),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
