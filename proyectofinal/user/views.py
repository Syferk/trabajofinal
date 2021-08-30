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
    student=UMODEL.Users.objects.get(user_id=request.user.id)
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

# Obtener puntajes y posicionamiento de ranking 
@login_required(login_url='userlogin')
@user_passes_test(is_user)
def calculate_marks_view(request):

    if request.POST.get('category_id') is not None:
        category_id = request.POST.get('category_id')
        category=QMODEL.Category.objects.get(id=category_id)
        total_marks = correctas = total_questions = 0
        marks_questions = 100/category.question_number
        ids_preguntas= request.POST.getlist('pregunta')
        questions=QMODEL.Question.objects.all().filter(id__in=ids_preguntas)
        for q in questions:
            selected_ans = request.POST.get(str(q.id))
            actual_answer = q.answer
            if selected_ans == actual_answer:
                total_marks = total_marks + marks_questions
                correctas = correctas + 1      #aumento la respuesta correcta
            total_questions += 1

        user = QMODEL.Users.objects.get(user_id=request.user.id)
        result = QMODEL.Result()
        result.marks=total_marks
        result.total_questions = total_questions
        result.exam=category
        result.user=user
        result.correct= correctas
        result.save()

        return redirect('check-marks', category.id)

@login_required(login_url='userlogin')
@user_passes_test(is_user)
def view_result_view(request):
    categories=QMODEL.Category.objects.all()
    contexto ={
        'categories':categories
    }
    return render(request,'user/view_result.html',contexto)

@login_required(login_url='userlogin')
@user_passes_test(is_user)
def check_marks_view(request,pk):
    category=QMODEL.Category.objects.get(id=pk)
    user = UMODEL.Users.objects.get(user_id=request.user.id)
    results= QMODEL.Result.objects.all().filter(exam=category).filter(user=user)
    return render(request,'user/check_marks.html',{'results':results})

@login_required(login_url='userlogin')
@user_passes_test(is_user)
def user_marks_view(request):
    categories=QMODEL.Category.objects.all()
    contexto ={
        'categories':categories
    }
    return render(request,'user/user_marks.html',contexto)

@login_required(login_url='userlogin')
@user_passes_test(is_user)
def ranking(request):
    users = UMODEL.Users.objects.all()
    lista = []
    for user in users:
        marks = 0
        results = QMODEL.Result.objects.all().filter(user = user)
        for result in results:
            marks += result.marks
        dict = {
            'user': user.get_username,
            'marks': marks,
        }
        lista.append(dict)
    contexto = {
        "lista": sorted(lista, key = lambda i: i['marks'],reverse=True),
    }
    return render(request, "user/ranking.html", contexto)