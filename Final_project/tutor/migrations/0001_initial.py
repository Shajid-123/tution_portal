# Generated by Django 5.0.1 on 2024-02-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('dob', models.CharField(max_length=500)),
                ('Phone', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('timings', models.CharField(max_length=500)),
                ('fee', models.CharField(max_length=500)),
                ('desc', models.TextField(max_length=5000)),
                ('grade', models.TextField(max_length=5000)),
            ],
        ),
    ]
