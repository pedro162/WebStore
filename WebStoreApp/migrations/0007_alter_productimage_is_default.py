# Generated by Django 5.0.7 on 2024-07-24 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("WebStoreApp", "0006_productimage_is_default"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="is_default",
            field=models.IntegerField(
                choices=[(1, "yes"), (0, "no")],
                default=0,
                help_text="This is the default image?",
                max_length=1,
            ),
        ),
    ]