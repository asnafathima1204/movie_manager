from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_page(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('list')
        else:
            error_message="invalid credential"
        
    return render(request,'users/login.html',{'error_message':error_message})

def logout_page(request):
    logout(request)
    return redirect('login')



def signup(request):
    user=None 
    error_message=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        try:
            user=User.objects.create_user(
                username=username,
                password=password
            )
        except Exception as e:
            error_message=str(e)
    return render(request,'users/create.html',{'user':user,'error_message':error_message})