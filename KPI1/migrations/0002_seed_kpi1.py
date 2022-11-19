from django.db import migrations

from KPI1.data import KPI1_list


def seed_KPI1(apps, schema_editor):
    for kpi1 in KPI1_list:
        kpi1.save()


class Migration(migrations.Migration):

    dependencies = [
        ('KPI1', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_KPI1)
    ]
