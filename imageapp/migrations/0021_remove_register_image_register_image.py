# Generated by Django 4.2.2 on 2023-07-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0020_alter_register_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="register",
            name="Image",
        ),
        migrations.AddField(
            model_name="register",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="data"),
        ),
    ]
