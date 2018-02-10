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
    path('dynamic-data-mech.html', views.dynamic_data_mech),
    path('lighting-sys-overview.html', views.lighting_sys_overview),
    path('lighting-sys-daylighting.html', views.lighting_sys_dl),
    path('lighting-sys-artificial.html', views.lighting_sys_al),
    path('dynamic-data-lighting.html', views.dynamic_data_lighting),
    path('sys-diagram-mech.html', views.sys_diagram_mech),
    path('sys-diagram-lighting.html', views.sys_diagram_lighting),
    path('sus-energy.html',views.sus_energy),
    path('sus-water.html',views.sus_water),
]
