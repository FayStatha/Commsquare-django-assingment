from django.db import migrations

from KPI2.data import KPI2_list


def seed_KPI2(apps, schema_editor):
    for kpi1 in KPI2_list:
        kpi1.save()


class Migration(migrations.Migration):

    dependencies = [
        ('KPI2', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_KPI2)
    ]
