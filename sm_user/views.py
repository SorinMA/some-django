# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required()
def stock_page(request):
    return render(request, 'sm_user/stock_page.html', {'user': request.user})

def home_page(request):
    return render(request, 'sm_user/home_page.html', {'user' : request.user})

