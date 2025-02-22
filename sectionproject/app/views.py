from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import registration
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

# Create your views here.
@never_cache
def home(request):
    if 'user' in request.session:
        current_user=request.session['user']
        param = {'current_user':current_user}
        return render(request,'base.html',param)
    else:
        return redirect('login')
    return render(request,'login.html')

def signup(request,):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        email=request.POST.get('email')
        ph=request.POST.get('phone')
        if registration.objects.filter(username=uname).count()>0:
            return HttpResponse('Username Already Exists')
        else:
            user=registration(username=uname,password=pwd,email=email,phone=ph)
            user.save()
            return redirect('login')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')

        check_user = registration.objects.filter(username=uname,password=pwd)
        if check_user:
            request.session['user']=uname
            return redirect('home')
        else:
            return HttpResponse("Please enter valid username or password.")
    return render(request,'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')