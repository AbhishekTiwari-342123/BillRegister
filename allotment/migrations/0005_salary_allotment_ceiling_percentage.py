# Generated by Django 3.2.7 on 2022-04-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allotment', '0004_alter_object_head_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary_allotment',
            name='Ceiling_Percentage',
            field=models.FloatField(default=0.5),
        ),
    ]