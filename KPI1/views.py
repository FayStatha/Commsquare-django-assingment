from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from KPI1.forms import GetKPI1ValidationForm
from KPI1.models import KPI1


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
        form = GetKPI1ValidationForm(request.GET)
        if not form.is_valid():
            return Response(
                status=400,
                data=f'Invalid query params values, error: {dict(form.errors)}'
            )

        query = KPI1.objects
        query_params = form.clean()

        try:
            if query_params['service_id']:
                query = query.filter(service_id=query_params['service_id'])
            if query_params['total_bytes']:
                query = query.filter(total_bytes=query_params['total_bytes'])
            if query_params['interval']:
                query = query.filter(interval=query_params['interval'])
            if query_params['interval_start_timestamp_ge']:
                query = query.filter(interval_start_timestamp__gte=query_params['interval_start_timestamp_ge'])
            if query_params['interval_start_timestamp_le']:
                query = query.filter(interval_start_timestamp__lte=query_params['interval_start_timestamp_le'])
            if query_params['interval_end_timestamp_ge']:
                query = query.filter(interval_end_timestamp__gte=query_params['interval_end_timestamp_ge'])
            if query_params['interval_end_timestamp_le']:
                query = query.filter(interval_end_timestamp__lte=query_params['interval_end_timestamp_le'])

            return Response(
                status=200,
                data=[kpi1_model_to_json(kpi1) for kpi1 in query.all()]
            )
        except Exception:
            return Response(
                status=500,
                data='Something went wrong. Try again later!'
            )
