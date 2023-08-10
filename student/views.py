from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout
from sport.models import LeaveRequest
from datetime import date, datetime
from .utils import generate_captcha
global log


def teacher_login(request):
   
    valuenext= request.POST.get('next') #

    if request.method=="POST":
        email1=request.POST.get('email')
        password1=request.POST.get('password')
        entered_captcha = request.POST.get('captcha', '')
        stored_captcha = request.session.get('captcha_text', '')
        
        try:
            user = Tregistration.objects.get(email=email1,password=password1)
            if entered_captcha != stored_captcha:
                global log
                log = True
                return redirect('teacher_home')
            else:
                # CAPTCHA is invalid
                # Display an error message
                error_message = "Invalid CAPTCHA. Please try again."
                return render(request, 'teacher_login.html', {'error_message': error_message})
            
            
        except Tregistration.DoesNotExist:
            error_message = "invalid username or password"
            return render(request,'teacher_login.html', {'error_message' : error_message})

    return render(request,'teacher_login.html')


def teacher_home(request):
    global log
    if log == True:
        cd = datetime.now()
        for i in LeaveRequest.objects.all():
            d1 = date(cd.year, cd.month, cd.day)
            d2 = date(i.date.year, i.date.month, i.date.day)
            delta = d1 - d2
            if delta.days >= 3:
                leave = LeaveRequest.objects.filter(date = i.date).first()
                leave.delete()

        ldata = LeaveRequest.objects.all()
        data = Reminder.objects.all()
        tdata = Timetable.objects.order_by('hnum')
        hnu = ['']
        hna = ['']
        tna = ['']
        for td in tdata:
            hnu.append(td.hnum)
            hna.append(td.hname)
            tna.append(td.tname)
        return render(request, "teacher_home.html", {'ldata' : ldata,'data': data, 'hnu': hnu, 'hna': hna, 'tna': tna})
    else:
        return redirect('teacher_login')


def delete_entry(request):
    global log
    if log == True:
        if request.method == 'POST':
            name = request.POST.get('name')
            try:
                entry = Reminder.objects.get(rname=name)
                entry.delete()
                return HttpResponse(status=200)
            except Reminder.DoesNotExist:
                return HttpResponse(status=404)
        return HttpResponse(status=400)
    else:
        return redirect('teacher_login')


def student(request):
    data = Reminder.objects.all()
    tdata = Timetable.objects.order_by('hnum')

    hna = ['']
    tna = ['']
    for td in tdata:
        hna.append(td.hname)
        tna.append(td.tname)

    return render(request, "student.html", {'data': data, 'hna': hna, 'tna': tna})


def ttform(request):
    global log
    if log == True:
        if request.method == 'POST':
            hn = request.POST.get('hnum')
            rows_to_update = Timetable.objects.filter(hnum=hn)
            hname = request.POST.get('hname')
            tname = request.POST.get('tname')

            for row in rows_to_update:
                row.hname = hname
                row.tname = tname
                row.save()
            return HttpResponseRedirect("")
        data = Reminder.objects.all()
        ldata = LeaveRequest.objects.all()
        tdata = Timetable.objects.order_by('hnum')
        hnu = ['']
        hna = ['']
        tna = ['']
        for td in tdata:
            hnu.append(td.hnum)
            hna.append(td.hname)
            tna.append(td.tname)
        return render(request, "teacher_home.html", {'ldata' : ldata,'data': data, 'hnu': hnu, 'hna': hna, 'tna': tna})
    else:
        return redirect('teacher_login')
    

def remform(request):
    global log
    if log == True:
        if request.method=="POST":
            name1=request.POST.get("name")
            date1=request.POST.get("date")
            data=Reminder(rname=name1,rdate=date1)
            data.save()
            return HttpResponseRedirect("")
        data = Reminder.objects.all()
        ldata = LeaveRequest.objects.all()
        tdata = Timetable.objects.order_by('hnum')
        hnu = ['']
        hna = ['']
        tna = ['']
        for td in tdata:
            hnu.append(td.hnum)
            hna.append(td.hname)
            tna.append(td.tname)
        return render(request, "teacher_home.html", {'ldata' : ldata,'data': data, 'hnu': hnu, 'hna': hna, 'tna': tna})
    else:
        return redirect('teacher_login')
    

def captcha_image(request):
    image, captcha_text = generate_captcha()
    response = HttpResponse(content_type='image/png')
    image.save(response, 'PNG')
    request.session['captcha_text'] = captcha_text  # Store the CAPTCHA text in the session
    return response


def tlogout_view(request):
    global log
    log = False
    logout(request)
    return redirect('teacher_login')


def visualize_data(request):
    global log
    if log == True:
        return render(request, 'visualize-data.html')
    else:
        return redirect('teacher_login')
