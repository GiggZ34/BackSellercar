# Generated by Django 5.0.9 on 2024-09-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='Seller_roles',
            field=models.CharField(choices=[('STANDARD', 'Standard'), ('OWNER', 'Owner')], max_length=30),
        ),
    ]
