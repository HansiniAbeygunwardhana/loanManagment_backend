# Generated by Django 4.2.1 on 2023-07-14 20:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loanarrears', '0003_rename_loan_loanarrears_loan_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanarrears',
            name='arr_cal_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
