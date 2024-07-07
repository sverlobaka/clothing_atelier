# Generated by Django 5.0.6 on 2024-07-06 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_textile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fabric",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
                ("sku", models.CharField(max_length=64, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "stock_meters",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.supplier",
                    ),
                ),
            ],
        ),
    ]
