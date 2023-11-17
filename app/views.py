from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import User  
from .models import *
from django.shortcuts import get_object_or_404, redirect


def signup(request):
    form = Createuserform
    if request.method == 'POST':
        form = Createuserform(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('signin')
    context = {'form':form}
    return render(request,'signup.html',context=context)

def signin(request):
    form = loginform
    if request.method == 'POST':
        form = loginform(request,data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('showdata')
    context = {"form":form}
    return render(request,'signin.html',context=context)


def dash(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        topic = request.POST.get('topic')
        description = request.POST.get('description')
        
        if not author or not topic or not description:
            return redirect('dash')
        
        notes = Notes(
            author=author,
            topic=topic,
            description=description
        )
        
        notes.save()
        return redirect('showdata')        
    return render(request,'dash.html')

def showdata(request):
    notes = Notes.objects.all()
    context = {'notes': notes}
    return render(request, 'showdata.html', context=context)

def delete_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)

    if request.method == 'POST':
        note.delete()

    return redirect('showdata')