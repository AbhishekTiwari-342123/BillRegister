# Generated by Django 3.2.7 on 2022-04-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allotment', '0005_salary_allotment_ceiling_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary_allotment',
            name='Year',
            field=models.IntegerField(default=2021),
        ),
    ]
