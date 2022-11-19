import datetime

from django.http import HttpResponseBadRequest
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
        interval='1-hour'
    ).save()
    KPI1(
        service_id=2,
        interval_end_timestamp=datetime.datetime.now(),
        interval_start_timestamp=datetime.datetime.now(),
        total_bytes=2,
        interval='5-minutes'
    ).save()


def kpi1_model_to_json(kpi1: KPI1) -> dict:
    return {
        'service_id': kpi1.service_id,
        'interval_start_timestamp': kpi1.interval_start_timestamp,
        'interval_end_timestamp': kpi1.interval_end_timestamp,
        'total_bytes': kpi1.total_bytes,
        'interval': kpi1.interval,
        'id': kpi1.id,
    }


class KPI1View(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        create_KPIS()

        query = KPI1.objects

        service_id = request.GET.get('service_id')
        total_bytes = request.GET.get('total_bytes')
        interval = request.GET.get('interval')
        interval_start_timestamp = request.GET.get('interval_start_timestamp')
        interval_end_timestamp = request.GET.get('interval_end_timestamp')

        try:
            if service_id:
                query = query.filter(service_id=service_id)
            if total_bytes:
                query = query.filter(total_bytes=total_bytes)
            if interval:
                query = query.filter(interval=interval)
            if interval_start_timestamp:
                query.filter(interval_start_timestamp=interval_start_timestamp)
            if interval_end_timestamp:
                query.filter(interval_end_timestamp=interval_end_timestamp)

            return Response([kpi1_model_to_json(kpi1) for kpi1 in query.all()])
        except Exception as e:
            raise HttpResponseBadRequest
