# Generated by Django 5.0.6 on 2024-09-25 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_customer_name_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Options', to='app.carmodel'),
        ),
    ]
