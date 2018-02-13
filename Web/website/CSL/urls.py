from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
    path('HVAC.html', views.HVAC),
    path('about.html', views.about),
    path('service.html', views.service),
    path('tbd.html', views.tbd),
    path('mech-sys-overview.html', views.mech_sys_overview),
    path('mech-sys-nv.html', views.mech_sys_nv),
    path('mech-sys-geo.html', views.mech_sys_geo),
    path('mech-sys-ufds.html', views.mech_sys_ufds),
    path('mech-sys-tcers.html', views.mech_sys_tcers),
    path('mech-sys-location.html', views.mech_sys_location),
    path('dynamic-data.html', views.dynamic_data),
    path('lighting-sys-overview.html', views.lighting_sys_overview),
    path('lighting-sys-daylighting.html', views.lighting_sys_dl),
    path('lighting-sys-artificial.html', views.lighting_sys_al),
    path('lighting-sys-location.html', views.lighting_sys_location),
    path('sys-diagram-mech.html', views.sys_diagram_mech),
    path('sys-diagram-lighting.html', views.sys_diagram_lighting),
    path('sustainability.html',views.sustainability),
    path('getRealTimeSupplyAirData/', views.getRealTimeSupplyAirData),
    path('getRealTimeOutdoorAirData/', views.getRealTimeOutdoorAirData),
    path('getRealTimeReturnedAirData/', views.getRealTimeReturnedAirData),
    path('getRealTimeMixedAirData/', views.getRealTimeMixedAirData),
    path('getHourTemperatureData/<int:hours>/<str:type>/', views.getHourTemperatureData),
    path('getTemperatureData/<str:startDate>/<str:endDate>/<str:type>/', views.getTemperatureData),
    path('getHumidityData/<str:startDate>/<str:endDate>/<str:type>/', views.getHumidityData),
    path('getFlowRateData/<str:startDate>/<str:endDate>/<str:type>/', views.getFlowRateData),
    ]
