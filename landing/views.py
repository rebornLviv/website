from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import *
from .forms import *

def home(request):

    slider = Slider.objects.filter(is_active=True)
    logos = LogoSlider.objects.filter(is_active=True)
    results = ResultBeyond.objects.filter(is_active=True)

    return render(request, 'landing/home.html', locals())