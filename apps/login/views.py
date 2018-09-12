# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def create(request):
    if request.method == "POST":
        user=User.object.creating_db(request.POST)
        if len(user)>0:
            context={
                "registration_error":1
            }
            for error in user:
                messages.error(request, error)
            return render(request,"login/index.html",context)
        else:
            print "created"
            return redirect('index:new')
    else:
            return redirect('index:new')

def log(request):
    if request.method == "POST":
        users=User.object.logging(request.POST)
        if type(users) == list:
            if len(users)>0:
                context = {
                    "login_error": 1
                }
                for error in users:
                    messages.error(request, error)
                return render(request,"login/index.html",context)
        else:
            user_id = str(users)
            if "user_id" not in request.session:
                request.session['user_id']=user_id
            context=User.object.selecting_user(user_id)
            return render(request,'login/success.html',context)
    else:
        if "user_id" in request.session:
            user_id=request.session['user_id']
            context=User.object.selecting_user(user_id)
            return render(request, 'login/success.html', context)
        else:
            return redirect('index:new')


def logout(request):
    if request.method == "POST":
        request.session.clear()
        return redirect("index:new")
    else:
        user_id = request.session['user_id']
        context = User.object.selecting_user(user_id)
        return render(request, 'login/success.html', context)


def wrong_num(request,user_id):
    return redirect('index:new')

def wrong_num_login(request,user):
    print user
    user_id = request.session['user_id']
    context = User.object.selecting_user(user_id)
    return render(request, 'login/success.html', context)

def nothing(request):
    print "ok"
    return redirect("index:new")

