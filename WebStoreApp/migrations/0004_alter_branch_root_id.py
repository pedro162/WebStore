# Generated by Django 5.0.7 on 2024-07-24 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WebStoreApp", "0003_alter_branch_active_alter_city_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branch",
            name="root_id",
            field=models.ForeignKey(
                blank=True,
                help_text="The root branch id",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="WebStoreApp.branch",
            ),
        ),
    ]
