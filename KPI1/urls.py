from django.urls import path
from KPI1.views import KPI1View

urlpatterns = [
    path('', KPI1View.as_view())
]
