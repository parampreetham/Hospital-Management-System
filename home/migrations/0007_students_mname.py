# Generated by Django 4.1.3 on 2023-01-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_students_father_students_mother"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="mname",
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
