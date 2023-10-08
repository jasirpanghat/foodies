# Generated by Django 4.1.5 on 2023-01-25 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('Customer_name', models.CharField(max_length=200, verbose_name='name')),
                ('Customer_email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('Customer_city', models.CharField(max_length=15, verbose_name='city')),
                ('Customer_country', models.CharField(max_length=300, verbose_name='country')),
            ],
        ),
    ]