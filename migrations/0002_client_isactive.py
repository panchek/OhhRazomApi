# Generated by Django 4.1 on 2022-10-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("OhhRazomApi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client", name="isActive", field=models.BooleanField(null=True),
        ),
    ]
