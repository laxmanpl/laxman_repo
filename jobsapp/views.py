from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyd_jobs_view(request):
    s = '<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(s)
def nzb_jobs_view(request):
    s = '<h1>Nizmabad Jobs Information</h1>'
    return HttpResponse(s)
def mubai_jobs_view(request):
    s = '<h1>Mubai Jobs Information</h1>'
    return HttpResponse(s)
def bng_jobs_view(request):
    s = '<h1>Bangalaru Jobs Information</h1>'
    return HttpResponse(s)
