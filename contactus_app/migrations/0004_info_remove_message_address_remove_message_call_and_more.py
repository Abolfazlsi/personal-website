# Generated by Django 5.0.6 on 2024-06-13 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contactus_app", "0003_message_address_message_call_message_email2_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Info",
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
                ("address", models.CharField(max_length=50)),
                ("call", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name="message",
            name="address",
        ),
        migrations.RemoveField(
            model_name="message",
            name="call",
        ),
        migrations.RemoveField(
            model_name="message",
            name="email2",
        ),
    ]
