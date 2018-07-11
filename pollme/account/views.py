from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import user_registration_form
from django.contrib.auth.models import User



# Create your views here.




def login_user(requset):
    if requset.method == "POST":
        username = requset.POST.get("username",None)
        password = requset.POST.get('password',None)
        user = authenticate(requset,username=username,password=password)
        if user is not None:
            login(requset, user)
            return redirect("polls:home")
        else:
            messages.error(requset,"thi is not")
    return render(requset,"login_user.html",locals())



def logout_user(requset):
    logout(requset)
    return HttpResponseRedirect(reverse("polls:home"))


def registration_form(request):
    if request.method == "POST":
        form = user_registration_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password1']
            email = form .cleaned_data['email']
            print(form.cleaned_data)
            user = User.objects.create_user(username,email=email,password=password)
            messages.success(request,'this is a new Genration')
            return HttpResponseRedirect(reverse("account:login_user"))
    else:
        form= user_registration_form()
    template_name = "registration_form.html"
    return render (request,template_name,{"form":form})
