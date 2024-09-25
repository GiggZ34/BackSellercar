# Generated by Django 5.0.6 on 2024-09-25 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('sell', models.BooleanField(default=False)),
                ('concession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cars_models', to='app.concession')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=0)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Options', to='app.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roles', models.CharField(choices=[('STANDARD', 'Standard'), ('OWNER', 'Owner')], max_length=30)),
                ('concession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.concession')),
            ],
        ),
        migrations.CreateModel(
            name='RelationSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_sells', to='app.carmodel')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_sells', to='app.customer')),
                ('options', models.ManyToManyField(related_name='relations_sells', to='app.option')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_sells', to='app.seller')),
            ],
        ),
    ]
