# Generated by Django 5.0.1 on 2024-02-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_tutor_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='v_c',
            field=models.TextField(default=1, max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tutor',
            name='v_status',
            field=models.TextField(default=1, max_length=5000),
            preserve_default=False,
        ),
    ]
