
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
global namer
global logger
# Create your views here.

def event(request):
    global logger
    if logger == True:
        return render(request, 'event.html')
    else:
        return redirect('login')

def notify(request):
    global logger
    if logger == True:
        if request.method == 'POST':
            # Process the form submission
            Date = request.POST.get('date')
            Leave_type = request.POST.get('leaveType')
            Reason = request.POST.get('reason')
            global namer
            try :
                Supporting_docs = request.FILES['supportingDocs']
                data = LeaveRequest(namelr =  namer, date = Date, leave_type =Leave_type, reason =Reason, supporting_docs = Supporting_docs,)
                data.save()
            except:
                data = LeaveRequest(namelr =  namer, date = Date, leave_type =Leave_type, reason =Reason,)
                data.save()
            return redirect('home')

        return render(request, 'notify.html')
    else:
        return redirect('login')


def registration(request):
    if request.method=="POST":
        name1=request.POST.get("name")
        email1=request.POST.get("email")
        password1=request.POST.get("password")
        confirmPassword1=request.POST.get("confirm-password")
        if(password1==confirmPassword1):
            try:
                data=Registration(name=name1,email=email1,password=password1)
                data.save() 
                return redirect('login')
            except:
                return redirect('registration')
        else:
            return redirect('registration')
        
    return render(request, 'registration.html')
    

def login(request):
   
    valuenext= request.POST.get('next') #

    if request.method=="POST":
        email1=request.POST.get('email')
        password1=request.POST.get('password')

        try:
            user = Registration.objects.get(email=email1,password=password1)
            global namer
            namer = user.name
            global logger
            logger = True
            return redirect('home')
        except Registration.DoesNotExist:
            error_message = "invalid username or password"
            return render(request,'login.html', {'error_message' : error_message})

    return render(request,'login.html')

def home(request):
    global logger
    if logger == True:
        return render(request, 'home.html')
    else:
        return redirect('login')

def logout_view(request):
    global logger
    logger = False
    logout(request)
    return redirect('login')


