# Generated by Django 5.0.1 on 2024-08-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("carts", "0003_cartitem_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
    ]