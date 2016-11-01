from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .dhlclient import *
from .forms import NewUserForm,BrokerUserForm

def home(request):
    if request.user.is_authenticated():
        title = 'Fuck Python ' + str(request.user)
    else:
        title = 'Log in'
    form = BrokerUserForm(request.POST or None)
    # if request.method == 'POST':
    #     print request.POST
    if form.is_valid():
        instance = form.save(commit=True)
        print instance.name
    context = {
        "bullshit":  title,
        "form": form
    }
    return render(request,"home.html",context)

def index(request):
    form = BrokerUserForm(request.POST or None)

    context = {
        "form": form
    }
    return render (request,"forms.html",context)

def tweets(request):
    context = {

    }
    return render (request,"tweets.html",context)

def new(request):
    form = NewUserForm(request.POST or None)

    if form.is_valid():
        for key,value in form.cleaned_data.iteritems():
            print key, value
    # send_mail('Django','Works',settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER],fail_silently=True)
    # DhlClient.call()
    nc = DhlClient()
    nc.establish
    context = {
        "form": form,
    }
    return render(request,"forms.html",context)