# Generated by Django 4.2.2 on 2024-09-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0005_alter_diary_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="diary",
            name="updated_at",
            field=models.DateField(
                auto_now=True, null="True", verbose_name="Дата изменения"
            ),
        ),
    ]
