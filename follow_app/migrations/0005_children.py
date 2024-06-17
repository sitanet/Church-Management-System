# Generated by Django 5.0.4 on 2024-06-11 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0004_nysc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=50)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member')),
            ],
        ),
    ]
