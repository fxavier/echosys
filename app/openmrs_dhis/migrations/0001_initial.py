# Generated by Django 3.2.5 on 2021-07-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenmrsOptimization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elegiveisdtg', models.IntegerField()),
                ('dtg_geral', models.IntegerField()),
                ('elegiveislpvr_geral', models.IntegerField()),
                ('dtg', models.IntegerField()),
                ('em_tarv', models.IntegerField()),
                ('lpvr', models.IntegerField()),
                ('elegiveis_lpvr', models.IntegerField()),
                ('elegiveisdtg_geral', models.IntegerField()),
                ('lpvr_geral', models.IntegerField()),
                ('us', models.CharField(max_length=100)),
                ('periodo', models.CharField(max_length=100)),
            ],
        ),
    ]