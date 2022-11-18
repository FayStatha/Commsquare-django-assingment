from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kpi1/', include('KPI1.urls')),
    path('kpi2/', include('KPI2.urls')),
]
