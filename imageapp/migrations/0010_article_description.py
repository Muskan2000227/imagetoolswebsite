# Generated by Django 4.2.2 on 2023-06-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("imageapp", "0009_editor"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="description",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
