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
            name='Colegiado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ciudad.Ciudad')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
