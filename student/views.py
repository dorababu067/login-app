from django.http import HttpResponse
from django.shortcuts import render,redirect
from student.forms import studentForm,studentInfo_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from student.models import *

# Create your views here.
def signIn(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login 
            user= form.get_user()
            login(request,user)
            return redirect('student')
        else:
            messages.warning(request,"Plz Check your username and password")
            return redirect('home')

    else:
        form = studentForm()
        return render(request,"login.html",{"form":form})

@login_required(login_url='home')
def student_view(request):
    if request.method == "POST":
        form = studentInfo_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect("details")
        else:
          return HttpResponse("data Iserted fail")
    else:
        form = studentInfo_form()
        return render(request,'student.html',{"form":form})

def student_details(request):
    data = studentInfo.objects.all()
    return render(request,"details.html",{"data":data})

def student_edit(request,id=None):
    #getting element from studentInfo Table
    data = studentInfo.objects.filter( id = id).get()
    if request.method == "POST":
        form = studentInfo_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('details')
    else:
        #passing the object in get request parameter
        form = studentInfo_form(instance=data)
        return render(request,'student.html',{"form":form})
        
def student_delete(request,id=None):
    #getting element from studentInfo Table
    data = studentInfo.objects.filter( id = id).get()
    data.delete()
    return redirect('details')


