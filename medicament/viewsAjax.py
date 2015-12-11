# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response,\
    redirect
from django.http import Http404

from django.http import HttpResponse
from django.template import RequestContext, loader   # исп для index2
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from medicament.models import Synchro


import os
import mimetypes
from django.template import response
import json
from concurrent.futures._base import wait
from time import sleep
from django.contrib.sessions.backends.db import SessionStore

_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(_PATH, 'documents', 'instruction')
MEDIA_URL = '/instruction/'

NUM_RECORD_ON_PAGE = 75   # число записей на странице списка

'''
def testAjax(request,question_id):
#    return HttpResponse("Hello, I am Ajax")
    for i in range(1,100000):
        for j in range(1,1000):
            k = i*j
        
    obj = { 'id' : 1234, 'name' : 'AndreyKayerov'}
    content = json.dumps(obj)
    response = HttpResponse(content)
#    response['Content-Type'] = 'text/javascript'
    return response 
'''
def testAjaxJQ(request,question_id):
   args = {} 
   return render_to_response("medicament/autoprogressbar-test.html", args)

def testAjaxJS1(request):
#
#    Тест 1 Передаваемые данные храним в спец таблице Synchro
#
    args = {} 
    return render_to_response("medicament/testJS1.html", args)

def testAjaxJS2(request):
#
#   Тест 2 Передаваемые данные храним в session, читаем, сохраняем как объект базы данных
#
    args = {} 
    return render_to_response("medicament/testJS2.html", args)

def serverCheck(request):
   print("serverCheck OK!") 
   return HttpResponse("OK")

def longOperation(request):
#    return HttpResponse("Hello, I am Ajax")
    print("serverLongOperation Start!")
#    return HttpResponse("OK")   
#
#Попытка хранить прогресс в session или cookies здесь не получится
#поскольку изменения фиксируются в базе session только при выходе - Response!!!
#поэтому прогресс я храню в спец базе Synchro
# ВАЖНО: можно попробовать работать с сессией как объектом базы данных и с метотом save() см. документацию django для session
#'''
    synObj = Synchro.objects.get(pk=1) 
    for i in range(0,101):
#        request.session['proc'] = str(i)
#        request.session['proc'] = i
#        print(request.session['proc'])
        synObj.val = i
        synObj.save();
        print("Set p=" + str(i))
#        for j in range(0,1000000):
#            k = i * j * i
        sleep(60)
    return HttpResponse("OK")           
    obj = { 'id' : 1234, 'name' : 'AndreyKayerov'}
    content = json.dumps(obj)
    response = HttpResponse(content)
    return response 

def longOperation2(request):
#    return HttpResponse("Hello, I am Ajax")
    print("serverLongOperation2 Start!")
#    return HttpResponse("OK")   
    s = SessionStore()     
    for i in range(0,101):
#        request.session['proc'] = str(i)
#        request.session['proc'] = i
#        print(request.session['proc'])
        s['proc'] = i
        s.save();
        print("Set p=" + str(i))
#        for j in range(0,1000000):
#            k = i * j * i
        sleep(1)
    return HttpResponse("OK")           
    obj = { 'id' : 1234, 'name' : 'AndreyKayerov'}
    content = json.dumps(obj)
    response = HttpResponse(content)
    return response 


def serverGetStatusOperation(request):
    proc = 0
    synObj = Synchro.objects.get(pk=1) 
    proc = synObj.val            
    obj = { 'proc' : proc,}
    content = json.dumps(obj)
    response = HttpResponse(content)
    return response 

def serverGetStatusOperation2(request):
    proc = 0
    if 'proc' in request.session:
       proc = request.session['proc']    
       obj = { 'proc' : proc,}
    
    
    content = json.dumps(obj)
    response = HttpResponse(content)
    return response 

