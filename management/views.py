from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic.base import View, TemplateView
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
def login_page(request):
    if request.POST:
        logout(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/management/')

    else:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return HttpResponseRedirect('/management/')
    return render_to_response('management/login.html', {}, context_instance=RequestContext(request))

class homepage(TemplateView):
    
    template_name = 'management/index.html'