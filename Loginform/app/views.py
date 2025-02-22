from django.shortcuts import render, redirect
from app.forms import loginform
from app.forms import checkform
from app.models import login_data


def register(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = loginform()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    message = ''
    if request.method == 'POST':
        form = checkform(request.POST)
        if form.is_valid():
            # Use request.POST.get() to retrieve the data
            username = request.POST.get('username')
            password = request.POST.get('password')

            try:
                # Authenticate by checking if the username and password exist in login_data
                data = login_data.objects.get(username=username, password=password)
                return redirect('/success')
                # message = "Login Successful!"
            except login_data.DoesNotExist:
                message = "Invalid Username or Password.Please Register"

            return render(request, 'login.html', {'form': form,'message':message})

    else:
        form = checkform()
    return render(request, 'login.html', {'form': form,'message':message})

def success(request):
    return render(request, 'success.html')
