import datetime

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from KPI1.models import KPI1


def create_KPIS():
    KPI1(
        service_id=1,
        interval_end_timestamp=datetime.datetime.now(),
        interval_start_timestamp=datetime.datetime.now(),
        total_bytes=8,
        interval='1H'
    ).save()
    KPI1(
        service_id=2,
        interval_end_timestamp=datetime.datetime.now(),
        interval_start_timestamp=datetime.datetime.now(),
        total_bytes=2,
        interval='5M'
    ).save()


def kpi1_model_to_json(kpi1: KPI1) -> dict:
    return {
        'service_id': kpi1.service_id,
        'interval_start_timestamp': kpi1.interval_start_timestamp,
        'interval_end_timestamp': kpi1.interval_end_timestamp,
        'total_bytes': kpi1.total_bytes,
        'interval': kpi1.interval,
    }


class KPI1View(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        create_KPIS()
        return Response([kpi1_model_to_json(kpi1) for kpi1 in KPI1.objects.all()])
