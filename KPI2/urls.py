from django.urls import path
from KPI2.views import KPI2View

urlpatterns = [
    path('', KPI2View.as_view())
]