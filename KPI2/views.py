import datetime
import uuid

from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from KPI2.models import KPI2


def create_KPIS2():
    KPI2(
        cell_id=uuid.uuid4(),
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

        query = KPI2.objects

        cell_id = request.GET.get('cell_id')
        number_of_unique_users = request.GET.get('number_of_unique_users')
        interval = request.GET.get('interval')
        interval_start_timestamp = request.GET.get('interval_start_timestamp')
        interval_end_timestamp = request.GET.get('interval_end_timestamp')

        try:
            if cell_id:
                query = query.filter(cell_id=cell_id)
            if number_of_unique_users:
                query = query.filter(number_of_unique_users=number_of_unique_users)
            if interval:
                query = query.filter(interval=interval)
            if interval_start_timestamp:
                query.filter(interval_start_timestamp=interval_start_timestamp)
            if interval_end_timestamp:
                query.filter(interval_end_timestamp=interval_end_timestamp)

            return Response([kpi2_model_to_json(kpi2) for kpi2 in query.all()])
        except Exception as e:
            raise HttpResponseBadRequest
