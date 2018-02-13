from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
import json

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

def dynamic_data(request):
    return render(request, 'CSL/template/dynamic-data.html')

def lighting_sys_overview(request):
    return render(request, 'CSL/template/lighting-sys-overview.html')

def lighting_sys_dl(request):
    return render(request, 'CSL/template/lighting-sys-daylighting.html')

def lighting_sys_al(request):
    return render(request, 'CSL/template/lighting-sys-artificial.html')

def lighting_sys_location(request):
    return render(request, 'CSL/template/lighting-sys-location.html')

def sys_diagram_mech(request):
    return render(request, 'CSL/template/sys-diagram-mech.html')

def sys_diagram_lighting(request):
    return render(request, 'CSL/template/sys-diagram-lighting.html')

def sustainability(request):
    return render(request, 'CSL/template/sustainability.html')


def getFromPi(url):
	# Never check any hostnames
	class HostNameIgnoringAdapter(HTTPAdapter):
	    def init_poolmanager(self, connections, maxsize, block=False):
	        self.poolmanager = PoolManager(num_pools=connections,
	                                       maxsize=maxsize,
	                                       block=block,
	                                       assert_hostname=False)
	s = requests.Session()
	s.mount('https://', HostNameIgnoringAdapter())
	r = s.get(
		url, auth=('CMU_Students', 'WorkHard!ChangeWorld'))
	r = json.loads(r.text);
	return r;

def getRealTimeSupplyAirData(request):
	r = getFromPi('https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ACzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9TVVBQTFkgQUlSIFRFTVAuUFJFU0VOVF9WQUxVRQ/value');
	return HttpResponse(r['Value'])

def getRealTimeOutdoorAirData(request):
	r = getFromPi('https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0AUjgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBPQVQgTU9OSVRPUl9PVVRTSURFIEFJUiBURU1QRVJBVFVSRS5QUkVTRU5UX1ZBTFVF/value');
	return HttpResponse(r['Value'])

def getRealTimeReturnedAirData(request):
	r = getFromPi('https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ABzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9SRVRVUk4gQUlSIFRFTVAuUFJFU0VOVF9WQUxVRQ/value');
	return HttpResponse(r['Value'])

def getRealTimeMixedAirData(request):
	r = getFromPi('https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ABDgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9NSVhFRCBBSVIgVEVNUC5QUkVTRU5UX1ZBTFVF/value');
	return HttpResponse(r['Value'])

def getHourTemperatureData(request, hours, type):
	now = datetime.utcnow();
	nowMXhr = now - timedelta(hours = hours);
	if type == "Supply":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ACzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9TVVBQTFkgQUlSIFRFTVAuUFJFU0VOVF9WQUxVRQ"
	elif type == "Fresh":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0AUjgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBPQVQgTU9OSVRPUl9PVVRTSURFIEFJUiBURU1QRVJBVFVSRS5QUkVTRU5UX1ZBTFVF"
	else:
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ABzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9SRVRVUk4gQUlSIFRFTVAuUFJFU0VOVF9WQUxVRQ"
	url = tmpURL + \
	      '/interpolated?starttime=%s&endtime=%s&interval=10m'%(nowMXhr.isoformat(), now.isoformat())
	r = getFromPi(url);
	retItems = r['Items'];
	formedTimeSeries = [];
	for retItem in retItems:
		if retItem["Good"]:
			formedTimeSeries.append([retItem["Timestamp"], retItem["Value"]]);
	response = {'Items': formedTimeSeries}
	return JsonResponse(response, json_dumps_params={'indent': 2})

def getTemperatureData(request, startDate, endDate, type):
	startTime = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
	endTime = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')
	if type == "Supply":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ACzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9TVVBQTFkgQUlSIFRFTVAuUFJFU0VOVF9WQUxVRQ"
	elif type == "Fresh":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0AUjgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMSBPQVQgTU9OSVRPUl9PVVRTSURFIEFJUiBURU1QRVJBVFVSRS5QUkVTRU5UX1ZBTFVF"
	else:
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ABzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9SRVRVUk4gQUlSIFRFTVAuUFJFU0VOVF9WQUxVRQ"
	url = tmpURL + \
	      '/interpolated?starttime=%s&endtime=%s&interval=10m'%(startTime.isoformat(), endTime.isoformat())
	r = getFromPi(url);
	retItems = r['Items'];
	formedTimeSeries = [];
	for retItem in retItems:
		if retItem["Good"]:
			formedTimeSeries.append([retItem["Timestamp"], retItem["Value"]]);
	response = {'Items': formedTimeSeries}
	return JsonResponse(response, json_dumps_params={'indent': 2})

def getHumidityData(request, startDate, endDate, type):
	startTime = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
	endTime = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')
	tmpURL = ""
	if type == "Fresh":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0AQTgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9PQSBIVU1JRElUWS5QUkVTRU5UX1ZBTFVF"
	elif type == "Returned":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0ARzgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9SQSBIVU1JRElUWS5QUkVTRU5UX1ZBTFVF"
	url = tmpURL + \
	      '/interpolated?starttime=%s&endtime=%s&interval=10m'%(startTime.isoformat(), endTime.isoformat())
	r = getFromPi(url);
	retItems = r['Items'];
	formedTimeSeries = [];
	for retItem in retItems:
		if retItem["Good"]:
			formedTimeSeries.append([retItem["Timestamp"], retItem["Value"]]);
	response = {'Items': formedTimeSeries}
	return JsonResponse(response, json_dumps_params={'indent': 2})

def getFlowRateData(request, startDate, endDate, type):
	startTime = datetime.strptime(startDate, '%Y-%m-%d %H:%M:%S')
	endTime = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')
	tmpURL = ""
	if type == "Supply":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0AKTgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9TVVBQTFkgQUlSRkxPVyBLQ0ZNLlBSRVNFTlRfVkFMVUU"
	elif type == "Fresh":
		tmpURL = "https://128.2.109.159/piwebapi/streams/P0-MYhSMORGkyGTe9bdohw0AJTgAAAV0lOLTYyTlBVMkJWTDIwXFBISVBQU19BSFUtMV9PVVRTSURFIEFJUkZMT1cgS0NGTS5QUkVTRU5UX1ZBTFVF"
	url = tmpURL + '/interpolated?starttime=%s&endtime=%s&interval=10m'%(startTime.isoformat(), endTime.isoformat())
	r = getFromPi(url);
	retItems = r['Items'];
	formedTimeSeries = [];
	for retItem in retItems:
		if retItem["Good"]:
			formedTimeSeries.append([retItem["Timestamp"], retItem["Value"]]);
	response = {'Items': formedTimeSeries}
	return JsonResponse(response, json_dumps_params={'indent': 2})
