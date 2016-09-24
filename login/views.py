from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Show login view
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Something wrong!")
                return redirect('login')
        else:
            messages.error(request, "Authentication Failed!")
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


# Logout
def logout(request):
    logout(request)
    messages.success(request, "You have successfully logout!")
    return redirect('/')