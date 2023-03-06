from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Mahesh(request):
    return HttpResponse("<marquee><h1 style='color:blue;'>my name is mahesh</h1></marquee>")
def Afrin(request):
    return HttpResponse('<marquee><h1 style="color:green;">mahesh babu will do always rocks</h1></marquee>')
def Greeshma(request):
    return HttpResponse('<marquee><h1 style="color:blue;">Greehma mam is my SQL Trainer</h1></marquee>')