from django.shortcuts import render,redirect
from chat.forms import CustomUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from rest_framework import authentication
from dotenv import load_dotenv
import openai,os
from openai import OpenAI
# Create your views here.
    

def home(request):
    return render(request,"chat/main.html")

def sign_in(request):
    if request.method=="POST":
        name = request.POST.get("username")
        pwd = request.POST.get("Password")
        user = authenticate(request,username = name, password = pwd)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged in Successfully")
            return redirect("/chat")
        else:
            messages.error(request,"Invalid username or password")
            return redirect('/sign_in')
    return render(request,"chat/sign_in.html")


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful You can login now..!")
            return redirect('/sign_in')
    return render(request,"chat/register.html",{'form':form})

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully...")
    return redirect('/home')


def chat(request):
    if request.method == 'POST':
        messages.success(request,"Still development in progress. We'll update you once we launch our application. Thank you for using our chatbot!")
        return redirect('/chat')
    return render(request,'chat/ChatUI.html')

    

 

    
