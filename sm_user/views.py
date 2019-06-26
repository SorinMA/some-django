# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

import requests
# Create your views here.


@login_required()
def stock_page(request):
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


    return render(request, 'sm_user/stock_page.html', {'user': request.user, 'date' : date, 'RON' : euro_to_ron, 'USD' : euro_to_usd, 'CHF' : euro_to_chf})

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
