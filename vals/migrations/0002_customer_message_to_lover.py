# Generated by Django 5.1.1 on 2025-02-03 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="message_to_lover",
            field=models.TextField(default="Hey [lover], I have..."),
        ),
    ]
