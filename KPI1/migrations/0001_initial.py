# Generated by Django 4.1.3 on 2022-11-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KPI1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.CharField(choices=[('1H', '1-hour'), ('5M', '5-minute')], max_length=2)),
            ],
        ),
    ]
