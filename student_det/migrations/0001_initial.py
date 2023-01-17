# Generated by Django 4.1.5 on 2023-01-16 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(default='', max_length=100)),
                ('degree', models.CharField(default='', max_length=100)),
                ('university', models.CharField(default='', max_length=100)),
                ('pro_email', models.CharField(default='', max_length=100)),
                ('linkedin', models.CharField(default='', max_length=100)),
                ('github', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('student_det', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_det.studentdet')),
            ],
        ),
        migrations.CreateModel(
            name='ProLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
                ('student_det', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='student_det.studentdet')),
            ],
        ),
    ]
