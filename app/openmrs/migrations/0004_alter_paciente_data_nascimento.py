# Generated by Django 3.2.5 on 2021-11-16 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openmrs', '0003_auto_20211116_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]