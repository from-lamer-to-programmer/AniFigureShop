# Generated by Django 5.0.1 on 2024-08-03 14:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0003_productimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderItem",
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
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Price"
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=0, verbose_name="Quantity"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Date of sell"
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="orders.order",
                        verbose_name="Order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to="products.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Проданный товар",
                "verbose_name_plural": "Проданные товары",
                "db_table": "order_item",
            },
        ),
    ]
