# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

def home_page(request):
    return  render(request, 'sm_user/home_page.html', {'user' : request.user})