from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        print("good")
        form=UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,str("Account Created for " + username),extra_tags="alert-success")
            return redirect('/')
    else:
        form=UserCreationForm
    return render(request,'signup.html',{'form': form})

def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Username or Password not correct",extra_tags="alert-danger")
        else:
            messages.error(request,"Username or Password not correct",extra_tags="alert-danger")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

#still have to make user to go to accounts.html instead of homepage i.e index.html
#------------------HERE------------------------------
@login_required()
def account(request):
    return redirect(request,'accounts.html')

@login_required()
def logout_request(request):
    logout(request)
    messages.success(request,"Logout successfull", extra_tags="alert-success")
    return redirect("/")

def home(request):
    return render(request,'index.html')