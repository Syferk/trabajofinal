from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group

# Create your views here.

def userclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'user/userclick.html')

def user_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.UserForm()
    contexto={
        'userForm':userForm,
        'studentForm':studentForm
    }
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.UserForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            user=studentForm.save(commit=False)
            user.user=user
            user.save()
            my_user_group = Group.objects.get_or_create(name='USER')
            my_user_group[0].user_set.add(user)
        return HttpResponseRedirect('userlogin')
    return render(request,'user/usersignup.html',contexto)


def is_user(user):
    return user.groups.filter(name='USER').exists()