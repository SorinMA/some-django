# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.decorators import login_required

from .forms import SignUpForm

from django.utils.encoding import force_bytes

from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string



# Create your views here.


@login_required()
def stock_page(request):
    return render(request, 'sm_user/stock_page.html', {'user': request.user})

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
