# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

import requests

import json

from time import gmtime, strftime

from django.http import JsonResponse

from .models import StockMarket
# Create your views here.




@login_required()
def stock_page(request):
    return render(request, 'sm_user/stock_page.html', {'user': request.user})

@login_required()
def stock_page_api(request):
    response = requests.get('https://api.exchangeratesapi.io/latest')
    curency = response.json()
    try:
        date = curency['date']
    except:
        date = '--/--/----'

    try:
        euro_to_ron = (curency['rates'])['RON']
    except:
        euro_to_ron = 0

    try:
        euro_to_usd = (curency['rates'])['USD']
    except:
        euro_to_usd = 0

    try:
        euro_to_chf = (curency['rates'])['CHF']
    except:
        euro_to_chf = 0

    data = {'date' : date, 'RON' : euro_to_ron, 'USD' : euro_to_usd, 'CHF' : euro_to_chf, 'value' : strftime("%Y-%m-%d %H:%M:%S", gmtime())}

    return JsonResponse(data, safe=False)

@login_required()
def stock_page_api_recive(request):
    if request.method == 'POST':
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa " + request.user.username + (request.body.decode('utf-8')))
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print ((body['value'])['RON'] )
        try:
            stock_values =  StockMarket.objects.create(stock_expert_player = request.user,
                                                   stock_RON = body['value']['RON'],
                                                   stock_USD = body['value']['USD'],
                                                   stock_CHF = body['value']['CHF'],
                                                   stock_msg = body['value']['message'],
                                                   stock_moment = body['value']['value'])
            stock_values.save()
        except:
            print("UPSSSS")
            return HttpResponse("OKn t")
        #StockMarket.objects.all().delete()  ups cmd
    return HttpResponse("OK")

@login_required()
def retrieve_strock_hist_db(request):
    values = StockMarket.objects.all().filter(stock_expert_player = request.user)
    print (values[0])
    data = []
    for i in values:
        data.append(i.get_RON())
    return JsonResponse(data, safe=False)

def home_page(request):
    return render(request, 'sm_user/home_page.html', {'user' : request.user})

def sm_registerx(request):
    form = SignUpForm()
    return render(request, 'sm_user/sm_register.html', {'user': request.user,
                                                        'form': form})
def sm_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return redirect('sm_login')
    else:
        form = SignUpForm()
    return render(request, 'sm_user/sm_register.html', {'user': request.user,
                                                        'form': form})
