from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'CSL/template/index.html')

def HVAC(request):
    return render(request, 'CSL/template/HVAC.html')

def about(request):
    return render(request, 'CSL/template/about.html')

def service(request):
    return render(request, 'CSL/template/service.html')

def tbd(request):
    return render(request, 'CSL/template/tbd.html')

def mech_sys_overview(request):
    return render(request, 'CSL/template/mech-sys-overview.html')

def mech_sys_nv(request):
    return render(request, 'CSL/template/mech-sys-nv.html')

def mech_sys_geo(request):
    return render(request, 'CSL/template/mech-sys-geo.html')

def mech_sys_ufds(request):
    return render(request, 'CSL/template/mech-sys-ufds.html')

def mech_sys_tcers(request):
    return render(request, 'CSL/template/mech-sys-tcers.html')
    
def mech_sys_location(request):
    return render(request, 'CSL/template/mech-sys-location.html')

def dynamic_data_mech(request):
    return render(request, 'CSL/template/dynamic-data-mech.html')
    
def lighting_sys_overview(request):
    return render(request, 'CSL/template/lighting-sys-overview.html')

def lighting_sys_dl(request):
    return render(request, 'CSL/template/lighting-sys-daylighting.html')
    
def lighting_sys_al(request):
    return render(request, 'CSL/template/lighting-sys-artificial.html')
    
def lighting_sys_location(request):
    return render(request, 'CSL/template/lighting-sys-location.html')
    
def dynamic_data_lighting(request):
    return render(request, 'CSL/template/dynamic-data-lighting.html')
    
def sys_diagram_mech(request):
    return render(request, 'CSL/template/sys-diagram-mech.html')

def sys_diagram_lighting(request):
    return render(request, 'CSL/template/sys-diagram-lighting.html')
    
def sus_energy(request):
    return render(request, 'CSL/template/sus-energy.html')
    
def sus_water(request):
    return render(request, 'CSL/template/sus-water.html')