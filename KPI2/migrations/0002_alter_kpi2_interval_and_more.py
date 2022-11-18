# Generated by Django 4.1.3 on 2022-11-18 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPI2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kpi2',
            name='interval',
            field=models.CharField(blank=True, choices=[('1H', '1-hour'), ('5M', '5-minute')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='kpi2',
            name='interval_end_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kpi2',
            name='interval_start_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]