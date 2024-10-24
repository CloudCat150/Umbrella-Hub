# Generated by Django 5.1.2 on 2024-10-24 16:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='rented_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rental',
            name='return_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='rental',
            name='student_number',
            field=models.CharField(max_length=10),
        ),
    ]