from django.shortcuts import render,redirect
from .models import Profile
from .forms import ProfileForm

def home(request):
    profile = Profile.objects.first()

    context = {
        'profile':profile,

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
