import datetime
import uuid

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from KPI2.forms import GetKPI2ValidationForm
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

        form = GetKPI2ValidationForm(request.GET)
        if not form.is_valid():
            return Response(
                status=400,
                data=f'Invalid query params values, error: {dict(form.errors)}'
            )

        query = KPI2.objects
        query_params = form.clean()

        try:
            if query_params['cell_id']:
                query = query.filter(cell_id=query_params['cell_id'])
            if query_params['number_of_unique_users']:
                query = query.filter(number_of_unique_users=query_params['number_of_unique_users'])
            if query_params['interval']:
                query = query.filter(interval=query_params['interval'])
            if query_params['interval_start_timestamp_ge']:
                query.filter(interval_start_timestamp__gte=query_params['interval_start_timestamp_ge'])
            if query_params['interval_start_timestamp_le']:
                query.filter(interval_start_timestamp__lte=query_params['interval_start_timestamp_le'])
            if query_params['interval_end_timestamp_ge']:
                query.filter(interval_end_timestamp__gte=query_params['interval_end_timestamp_ge'])
            if query_params['interval_end_timestamp_le']:
                query.filter(interval_end_timestamp__lte=query_params['interval_end_timestamp_le'])

            return Response([kpi2_model_to_json(kpi2) for kpi2 in query.all()])
        except Exception:
            return Response(
                status=500,
                data='Something went wrong. Try again later!'
            )
