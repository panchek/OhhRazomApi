# Generated by Django 4.1 on 2022-10-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("OhhRazomApi", "0003_rk_stage_rk_create_date_rk_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rk", name="end_date", field=models.DateTimeField(),
        ),
    ]
