# Generated by Django 4.1.5 on 2023-01-25 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frenchcafe', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='Log_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='frenchcafe.log'),
            preserve_default=False,
        ),
    ]
