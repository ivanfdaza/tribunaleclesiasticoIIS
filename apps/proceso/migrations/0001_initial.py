# Generated by Django 2.1.1 on 2020-07-17 20:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colegiado', '0001_initial'),
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diocesi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('radicado', models.IntegerField(primary_key=True, serialize=False)),
                ('expediente', models.CharField(default=None, max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('observacion', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('defensor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person2', to='colegiado.Colegiado')),
                ('demandado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person6', to='persona.Persona')),
                ('demandante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person5', to='persona.Persona')),
                ('diocesis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proceso.Diocesi')),
                ('juez1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person3', to='colegiado.Colegiado')),
                ('juez2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person4', to='colegiado.Colegiado')),
                ('notario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person7', to='colegiado.Colegiado')),
                ('presidente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person1', to='colegiado.Colegiado')),
            ],
            options={
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='proceso',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proceso.Tipo'),
        ),
    ]
