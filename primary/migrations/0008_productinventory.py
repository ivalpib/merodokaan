# Generated by Django 5.1 on 2024-09-13 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0007_delete_productinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('expiry_date', models.DateField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary.product')),
            ],
        ),
    ]
