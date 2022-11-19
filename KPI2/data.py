import uuid

from KPI2.models import KPI2

KPI2_list = [
    KPI2(
        cell_id=uuid.uuid4(),
        interval_end_timestamp=1668885266915,
        interval_start_timestamp=1668885266920,
        number_of_unique_users=8,
        interval='1-hour'
    ),
    KPI2(
        cell_id=uuid.uuid4(),
        interval_end_timestamp=1768885266915,
        interval_start_timestamp=1768885266915,
        number_of_unique_users=12,
        interval='5-minute'
    ),
]