# Generated by Django 3.2.5 on 2021-11-17 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openmrs', '0009_auto_20211116_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultaclinica',
            name='peso',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
