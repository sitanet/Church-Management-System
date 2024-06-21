# Generated by Django 3.2.20 on 2024-06-19 21:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField(blank=True, null=True)),
                ('achievements_and_awards', models.TextField(blank=True, null=True)),
                ('additional_information', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=52)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=52)),
                ('phone_no', models.CharField(max_length=15)),
                ('gender', models.PositiveIntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('marital_status', models.PositiveIntegerField(choices=[(1, 'Single'), (2, 'Married'), (3, 'Teenager'), (4, 'Children')])),
                ('occupation', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=20)),
                ('kcc_center', models.CharField(blank=True, max_length=20, null=True)),
                ('place_of_work', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.CharField(blank=True, max_length=40, null=True)),
                ('wedding_ann', models.DateField(blank=True, null=True)),
                ('join', models.DateField(blank=True, null=True)),
                ('about', models.CharField(blank=True, max_length=20, null=True)),
                ('dept', models.CharField(blank=True, max_length=20, null=True)),
                ('purpose', models.CharField(blank=True, max_length=20, null=True)),
                ('team_lead', models.CharField(blank=True, max_length=20, null=True)),
                ('team_member', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.PositiveIntegerField(blank=True, choices=[(1, 'Active'), (2, 'Inactive')], default='1')),
                ('kin_fullname', models.CharField(blank=True, max_length=50, null=True)),
                ('kin_birth', models.DateField(blank=True, null=True)),
                ('kin_gender', models.CharField(blank=True, max_length=20, null=True)),
                ('kin_relationship', models.CharField(blank=True, max_length=20, null=True)),
                ('kin_address', models.CharField(blank=True, max_length=100, null=True)),
                ('kin_phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('kin_email', models.CharField(blank=True, max_length=50, null=True)),
                ('emergency_phone_no', models.CharField(blank=True, max_length=20, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('team_lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.team_lead')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_address', models.CharField(max_length=255)),
                ('parent_phone_number', models.CharField(max_length=15)),
                ('university_name', models.CharField(max_length=255)),
                ('program_of_study', models.CharField(max_length=255)),
                ('program', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')], max_length=2)),
                ('work_type', models.CharField(choices=[('Internship', 'Internship'), ('Part-time job', 'Part-time job')], max_length=50)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='PreviousEmployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.career')),
            ],
        ),
        migrations.CreateModel(
            name='Pastorate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OtherQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification', models.CharField(blank=True, max_length=100, null=True)),
                ('institution', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_graduation', models.PositiveIntegerField(blank=True, null=True)),
                ('gpa', models.FloatField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.career')),
            ],
        ),
        migrations.CreateModel(
            name='NYSC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_address', models.CharField(max_length=255)),
                ('parent_phone_number', models.CharField(max_length=20)),
                ('university_name', models.CharField(max_length=100)),
                ('program_of_study', models.CharField(max_length=100)),
                ('year_of_graduation', models.IntegerField()),
                ('place_of_assignment', models.CharField(max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=100)),
                ('team_lead', models.CharField(blank=True, max_length=20, null=True)),
                ('team_member', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(max_length=255)),
                ('husband', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='husband', to='follow_app.member')),
                ('wife', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wife', to='follow_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='EducationalBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('institution', models.CharField(blank=True, max_length=100, null=True)),
                ('year_of_graduation', models.PositiveIntegerField(blank=True, null=True)),
                ('gpa', models.FloatField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.career')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentEmployment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('responsibilities', models.TextField(blank=True, null=True)),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_employments', to='follow_app.career')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=25, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=25, null=True)),
                ('team_mem', models.CharField(blank=True, max_length=50, null=True)),
                ('coor_comm', models.CharField(blank=True, max_length=30, null=True)),
                ('date_created', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('comment', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='follow_app.member')),
                ('team_sup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=50)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member')),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='follow_app.family')),
            ],
        ),
        migrations.AddField(
            model_name='career',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=255)),
                ('is_registered', models.BooleanField(default=False, verbose_name='Is business registered')),
                ('brief_description', models.TextField(blank=True)),
                ('years_of_experience', models.PositiveIntegerField(default=0, verbose_name='Years of business experience')),
                ('number_of_employees', models.PositiveIntegerField(default=1)),
                ('business_sector', models.CharField(choices=[('Technology', 'Technology'), ('Finance', 'Finance'), ('Healthcare', 'Healthcare'), ('Education', 'Education'), ('Manufacturing', 'Manufacturing'), ('Real Estate', 'Real Estate'), ('Hospitality', 'Hospitality'), ('Retail', 'Retail'), ('Entertainment', 'Entertainment')], max_length=100)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follow_app.member')),
            ],
        ),
    ]
