# Generated by Django 5.0.1 on 2024-08-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0002_alter_cart_product_cartitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]