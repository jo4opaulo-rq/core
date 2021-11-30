# Generated by Django 3.2.9 on 2021-11-30 17:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClientModel",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=55, verbose_name="Name")),
                ("email", models.EmailField(max_length=100, verbose_name="Email")),
            ],
        )
    ]
