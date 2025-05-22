from django.shortcuts import render,redirect
from .models import *
from .forms import ProfileForm
from datetime import datetime

def home(request):
    profile = Profile.objects.first()
    about = AboutMe.objects.all()
    skill = Skill.objects.all()
    project = Project.objects.all()
    testimonials = Testimonials.objects.all() 
    journey = Journey.objects.all() 
    current_year = datetime.now().year
    total_project = project.count()
    context = {
        'profile':profile,
        'about':about,
        'skill':skill,
        'project':project,
        'testimonials':testimonials,
        'journey':journey,
        'current_year':current_year,
        'total_project':total_project,
        
    }

    return render(request,'index.html',context)

def add_details(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_details')
    else:
        form = ProfileForm()
    return render(request,'add_details.html',{'form':form})
