from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    return render(request, 'user/home.html', context)

def login(request):
    context={}
    return render(request, 'registration/login.html', context)

def reguser(request):
    context={}
    return render(request, 'registration/reguser.html', context)

#def edituser(request):
#    context={}
#    return render(request, 'registration/edituser.html', context)