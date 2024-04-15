# Generated by Django 5.0.4 on 2024-04-11 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('immatriculation', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('marque', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('proprietaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiara.personne')),
            ],
        ),
    ]
