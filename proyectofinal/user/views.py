from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from . import forms
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from quiz import models as QMODEL
from user import models as UMODEL
from django.contrib.auth import models


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

@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_dashboard_view(request):
    contexto={
    'total_category':QMODEL.Category.objects.all().count(),
    'total_question':QMODEL.Question.objects.all().count(),
    }
    return render(request,'user/user_dashboard.html',contexto)

# Decoradores
@login_required(login_url='userlogin')
@user_passes_test(is_user)
def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect("userlogin")
    perfil = request.user
    student=UMODEL.User.objects.get(user_id=request.user.id)
    user=models.User.objects.get(id=student.user_id)
    userForm=forms.StudentUserForm(instance=user)
    studentForm=forms.UserForm(request.FILES,instance=student)
    if request.method == "POST":
        userForm=forms.StudentUserForm(request.POST, instance=user)
        studentForm=forms.UserForm(request.POST, request.FILES,instance=student)
        if studentForm.is_valid() and userForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            studentForm.save()
            return redirect("user-dashboard")
    contexto = {"userForm":userForm, "studentForm": studentForm}
    return render(request, "user/edit_profile.html",contexto)

@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_exam_view(request):
    categories=QMODEL.Category.objects.all().filter(question_available__gte = QMODEL.Category.objects.all().values('question_number'))
    contexto = {
        'categories': categories
    }
    return render(request,'user/user_exam.html',contexto)