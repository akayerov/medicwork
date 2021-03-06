from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import Http404

from django.http import HttpResponse
from django.template import RequestContext, loader   # исп для index2

import os
from django.core.context_processors import request
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
# выше базовое использоавлось ранее и было скопировано
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
             args['login_error'] = "Пользователь не найден"
             return render_to_response('login.html', args)
    return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect("/")

def registeruser(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm();
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            user1 = newuser_form.cleaned_data['username']
            password1 = newuser_form.cleaned_data['password2']
            user = auth.authenticate(username=user1,password=password1) 
            auth.login(request, user)
            return redirect("/")
        else:
            args['form'] = newuser_form
            return render_to_response('register.html', args)
       
    return render_to_response('register.html', args)

