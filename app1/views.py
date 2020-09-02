from django.shortcuts import render
from app1.forms import UserForm,UserProfileInfoForm,UserProfileTeacherInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
#from app1.backends import EmailBackend
# Create your views here.
def index(request):
    return render(request,'app1/index.html')

def register(request):
    return render(request,'app1/choice.html')

def register_student(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()


            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()
            registered=True
        else:
            print(user_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()


    return render(request,'app1/registration.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered
                    })
def register_teacher(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileTeacherInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()


            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()
            registered=True
        else:
            print(user_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileTeacherInfoForm()


    return render(request,'app1/teacher.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered
                    })


def user_login(request):

    if request.method=="POST":

        email=request.POST.get('email')
        password=request.POST.get('Password')
        user=authenticate(email=email,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("INVALID LOGIN DETAILS SUPPLIED")
    else:
        return render(request,'app1/user_login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse('YOU R LOGGED IN')
