from django.shortcuts import render
from .models import Hurriyet,Cumhuriyet,Birgun,Milliyet
# Create your views here.
def gazete_list(request):

    return render(request ,'koseyazi/gazete_list.html',{})


def hurriyet_yazilar(request):
    koseler = Hurriyet.objects.all()
    return render(request,'koseyazi/hurriyet_yazilar.html',{'koseler':koseler})

def milliyet_yazilar(request):
    koseler = Milliyet.objects.all()
    return render(request,'koseyazi/milliyet_yazilar.html',{'koseler':koseler})

def cumhuriyet_yazilar(request):
    koseler = Cumhuriyet.objects.all()
    return render(request,'koseyazi/cumhuriyet_yazilar.html',{'koseler':koseler})

def birgun_yazilar(request):
    koseler = Birgun.objects.all()
    return render(request,'koseyazi/birgun_yazilar.html',{'koseler':koseler})