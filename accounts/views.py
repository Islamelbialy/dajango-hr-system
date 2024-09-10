from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate ,update_session_auth_hash
from .forms import signUpForm
# Create your views here.

def signUp(req):
    form = signUpForm()
    if req.method == 'POST':
        form = signUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            auth_login(req,user)
            return redirect('Branches')
    return render(req,"accounts/signUp.html",{'form':form})

def logout(req):
    auth_logout(req)
    return redirect('Branches')

def login(req):
    form = AuthenticationForm()
    next = ''
    if req.GET:
        next = req.GET['next']
    if req.method == 'POST':
            form = AuthenticationForm(req,req.POST)
            print(form.errors)
            if form.is_valid():
                username = req.POST["username"]
                password = req.POST["password"]
                user = authenticate(req, username=username, password=password)
                # print("---------",user)
                if user is not None:
                    print("ewfewfewf")
                    auth_login(req,user)
                    if next == '':
                        return redirect('Branches')
                    else:
                        return HttpResponseRedirect(next)
            else:
                print("dsfmdsovods")
                return render(req,"accounts/login.html",{'form':form,'error':form.errors})
    return render(req,"accounts/login.html",{'form':form})

def changePassword(req):
    form = PasswordChangeForm(req.user)
    if req.method == "POST":
        form = PasswordChangeForm(user=req.user, data=req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('Branches')
    return render(req,"accounts/changePassword.html",{'form':form})

