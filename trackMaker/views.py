from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache


def home1(request):
    return render(request,'home1.html')


def registration1(request):
    if request.method=="POST":
        name1=request.POST.get("name")
        email1=request.POST.get("email")
        password1=request.POST.get("password")
        confirmPassword1=request.POST.get("confirm-password")
        insta1=request.POST.get("socials-id")
        if(password1==confirmPassword1):
            data=Registration(name=name1,email=email1,password=password1,confirmPassword=confirmPassword1,insta=insta1)
            data.save() 
            return redirect('login1')
        else:
            return redirect('registration1')
    return render(request,'registration1.html')

def login1(request):
   
    if request.method=="POST":
        email1=request.POST.get('email')
        password1=request.POST.get('password')

        try:
            user = Registration.objects.get(email=email1,password=password1)
            return redirect('logged_home')
        except Registration.DoesNotExist:
            error_message = "Invalid username or password"
            return render(request,'login1.html', {'error_message' : error_message})

    return render(request,'login1.html')

def logged_home(request):
        return render(request,'logged_home.html')

def track_home(request):
    return render(request,'track_home.html')


# Create your views here.
def logged_home(request):
    
    return render(request,'logged_home.html')

def track_home(request):
    return render(request,'track_home.html')

def songPublish(request):
    if request.method=="POST":
        artist=request.POST.get('artist')
        title=request.POST.get('title')
        song=request.FILES.get('audio')
        data=Songs(s_title=title,songs=song,s_artist=artist)
        data.save()
        #messages.success(request,"File Successfully Uploaded")
        return redirect(track_home)
    return render(request,'songPublish.html')

def makeRequest(request):
    if request.method=="POST":
        artist=request.POST.get('artist')
        title1=request.POST.get('title')
        track=request.FILES.get('audio')
        data=MusicFiles(title=title1,song=track,artist=artist)
        data.save()
        return HttpResponse('Successfully Uploaded')# return redirect
    return render(request,'makeRequest.html')

def viewRequest(request):
    tracks = MusicFiles.objects.all()
    return render(request, 'viewRequest.html', {'tracks': tracks})
    
def listen(request):
    tracks = Songs.objects.all()
    return render(request, 'listen.html', {'tracks': tracks})

@never_cache
def logout_track(request):
    global logger
    logger = False
    logout(request)
    return redirect('login1')
