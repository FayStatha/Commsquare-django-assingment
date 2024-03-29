# Generated by Django 4.1.3 on 2022-11-19 01:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KPI1',
            fields=[
                ('interval_start_timestamp', models.FloatField(blank=True, null=True)),
                ('interval_end_timestamp', models.FloatField(blank=True, null=True)),
                ('service_id', models.IntegerField(blank=True, null=True)),
                ('total_bytes', models.IntegerField(default=0)),
                ('interval', models.CharField(blank=True, choices=[('1-hour', 'One Hour'), ('5-minutes', 'Five Minute')], max_length=10, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
    ]
