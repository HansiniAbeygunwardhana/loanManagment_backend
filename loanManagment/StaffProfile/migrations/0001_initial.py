# Generated by Django 4.2.1 on 2023-07-12 07:44

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
            name='StaffProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('surname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('telephone1', models.CharField(max_length=100)),
                ('telephone2', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField(null=True)),
                ('nicnumber', models.CharField(max_length=100)),
                ('branch', models.CharField(choices=[('Polonnaruwa', 'Polonnaruwa'), ('Hingurakgoda', 'Hingurakgoda'), ('Diyasenpura', 'Diyasenpura'), ('Sewanapitiya', 'Sewanapitiya'), ('Dehiaththakandiya', 'Dehiaththakandiya'), ('Mahiyanganaya', 'Mahiyanganaya')], default='Sewanapitiya', max_length=20)),
                ('is_collector', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
