# Generated by Django 4.2.1 on 2023-06-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_remove_loan_loan_name_alter_loan_branch_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='loan_number',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
