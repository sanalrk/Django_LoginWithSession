from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache

# Create your views here.
def home(request):
    return render(request,"home.html",{})

@never_cache
def login(request):
    valid_email = 'admin@gmail.com'
    valid_password = 'password'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == valid_email and password == valid_password:
            request.session['email'] = email
            return redirect('dashboard')
        else:
            error_msg = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_msg})      
    return render(request,"login.html",{})

@never_cache
def dashboard(request):
    email = request.session.get('email')
    if email:
        return render(request, 'index.html',{'email': email})
    else:
        return redirect('login')

@never_cache
def signout(request):
    request.session.clear()
    return redirect('login')