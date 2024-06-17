# Generated by Django 5.0.4 on 2024-06-11 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('follow_app', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='NYSC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_address', models.CharField(max_length=255)),
                ('parent_phone_number', models.CharField(max_length=20)),
                ('university_name', models.CharField(max_length=100)),
                ('program_of_study', models.CharField(max_length=100)),
                ('year_of_graduation', models.IntegerField()),
                ('place_of_assignment', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member')),
            ],
        ),
    ]
