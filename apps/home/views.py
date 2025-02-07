
from asyncio.log import logger
from collections import UserList
from email.utils import formatdate
from multiprocessing import context
#from logging.config import _RootLoggerConfiguration
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from datetime import datetime
from .models import Eveniment, Voluntari
from requests import request
from .forms import FormularVol

def add_vol(request): 
    date = FormularVol(request.POST, request.FILES)
    print(request.FILES)
    return render(request, 'home/contact.html', {'date':date})
   

def all_volunteers(request):
    logger.info('**************************')

    volunteers = Voluntari.objects.all()
    return render(request,'home/voluntari.html', {'volunteers': volunteers})

def all_events(request):
    logger.info('**************************')

    event = Eveniment.objects.all()
    return render(request,'home/', {'event': event}) 


def index(request):
    current_datetime = datetime.now().date()  
    return render(request,'/dashboard.html', {'current_datetime':current_datetime})

  

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/dashboard.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


