# Generated by Django 5.1.1 on 2024-09-28 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='status.statusgeneral')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producttype')),
            ],
        ),
    ]