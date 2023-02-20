# Generated by Django 4.1.5 on 2023-02-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internship', '0002_internship_closing_date_internship_open_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateField()),
                ('closing_date', models.DateField()),
                ('Internship', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='internship.internship')),
            ],
        ),
    ]