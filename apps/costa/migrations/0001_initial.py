# Generated by Django 2.1.1 on 2020-07-17 20:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proceso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costa',
            fields=[
                ('proceso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='proceso.Proceso')),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('abonado', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('deuda', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=19)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
    ]
