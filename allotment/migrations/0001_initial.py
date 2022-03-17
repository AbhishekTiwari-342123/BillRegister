# Generated by Django 3.2.7 on 2022-03-17 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major_Sub_Head',
            fields=[
                ('Head_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('SubHead_Code', models.IntegerField(default=0, unique=True)),
                ('Head_Name', models.CharField(default='', max_length=250)),
                ('SubHead_Name', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MinorScheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MinorHead_Code', models.IntegerField()),
                ('Scheme_Code', models.IntegerField()),
            ],
            options={
                'unique_together': {('MinorHead_Code', 'Scheme_Code')},
            },
        ),
        migrations.CreateModel(
            name='Object_Head',
            fields=[
                ('Object_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('Object_Name', models.CharField(default='', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Salary_Allotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Allotment_Amount', models.IntegerField(default=0)),
                ('Object_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.object_head', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('Scheme_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('Scheme_Name', models.CharField(default='', max_length=250)),
                ('MinorHead_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.minorscheme')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Scheme',
            fields=[
                ('SubScheme_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('SubScheme_Name', models.CharField(default='', max_length=250)),
                ('Scheme_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.scheme')),
            ],
        ),
        migrations.CreateModel(
            name='Salary_Register',
            fields=[
                ('Bill_Number', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Description', models.TextField(default='', max_length=300)),
                ('Bill_Date', models.DateField()),
                ('Bill_Amount', models.IntegerField(default=0)),
                ('Bill_Expenditure', models.IntegerField(default=0)),
                ('Bill_Balance', models.IntegerField(default=0)),
                ('Bill_Remark', models.CharField(default='', max_length=250)),
                ('Bill_Type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.salary_allotment', to_field='Object_Code')),
            ],
        ),
        migrations.AddField(
            model_name='object_head',
            name='SubScheme_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.sub_scheme'),
        ),
        migrations.CreateModel(
            name='Minor_Head',
            fields=[
                ('MinorHead_Code', models.IntegerField(primary_key=True, serialize=False)),
                ('MinorHead_Name', models.CharField(default='', max_length=250)),
                ('Head_Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allotment.major_sub_head')),
            ],
        ),
    ]
