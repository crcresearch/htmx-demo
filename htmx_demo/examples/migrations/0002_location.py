# Generated manually for examples app - Location model

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("examples", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
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
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(blank=True, max_length=300)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("restaurant", "Restaurant"),
                            ("hotel", "Hotel"),
                            ("museum", "Museum"),
                            ("park", "Park"),
                            ("shopping", "Shopping"),
                            ("office", "Office"),
                        ],
                        default="restaurant",
                        max_length=50,
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("rating", models.DecimalField(decimal_places=1, default=0.0, max_digits=2)),
                (
                    "price_range",
                    models.CharField(
                        choices=[
                            ("$", "Budget"),
                            ("$$", "Moderate"),
                            ("$$$", "Expensive"),
                            ("$$$$", "Very Expensive"),
                        ],
                        default="$$",
                        max_length=4,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
    ]

