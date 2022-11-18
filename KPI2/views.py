import datetime

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from KPI2.models import KPI2


def create_KPIS2():
    KPI2(
        cell_id=1,
        interval_end_timestamp=datetime.datetime.now(),
        interval_start_timestamp=datetime.datetime.now(),
        number_of_unique_users=8,
        interval='1H'
    ).save()


def kpi2_model_to_json(kpi2: KPI2) -> dict:
    return {
        'cell_id': kpi2.cell_id,
        'interval_start_timestamp': kpi2.interval_start_timestamp,
        'interval_end_timestamp': kpi2.interval_end_timestamp,
        'number_of_unique_users': kpi2.number_of_unique_users,
        'interval': kpi2.interval,
    }


class KPI2View(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        create_KPIS2()
        return Response([kpi2_model_to_json(kpi2) for kpi2 in KPI2.objects.all()])
