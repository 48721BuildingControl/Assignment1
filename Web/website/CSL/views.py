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