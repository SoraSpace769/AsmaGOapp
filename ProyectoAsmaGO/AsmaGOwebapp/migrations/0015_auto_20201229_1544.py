# Generated by Django 3.1.3 on 2020-12-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsmaGOwebapp', '0014_auto_20201229_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='ataques',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='medicacion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='sintomas_diurnos',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students',
            name='sintomas_nocturnos',
            field=models.CharField(max_length=255),
        ),
    ]
