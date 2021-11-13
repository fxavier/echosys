# Generated by Django 3.2.5 on 2021-07-09 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('openmrs_dhis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='openmrsoptimization',
            name='province',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.province'),
            preserve_default=False,
        ),
    ]
