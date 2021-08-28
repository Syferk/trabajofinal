from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from user import models as UMODEL
from . import models, forms

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'quiz/index.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={
    'total_user':UMODEL.Users.objects.all().count(),
    'total_category':models.Category.objects.all().count(),
    'total_question':models.Question.objects.all().count(),
    }
    return render(request,'quiz/admin_dashboard.html',context=dict)


# Lógica para cargar, actualizar y eliminar categorías
@login_required(login_url='adminlogin')
def admin_category_view(request):
    return render(request,'quiz/admin_category.html')

@login_required(login_url='adminlogin')
def admin_add_category_view(request):
    categoryForm=forms.CategoryForm()
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST)
        if categoryForm.is_valid():        
            categoryForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-add-question')
    return render(request,'quiz/admin_add_category.html',{'categoryForm':categoryForm})


@login_required(login_url='adminlogin')
def admin_view_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'quiz/admin_view_category.html',{'categories':categories})

@login_required(login_url='adminlogin')
def admin_update_category_view(request, pk):
    categories = models.Category.objects.get(id=pk)
    categoryForm = forms.CategoryForm(instance=categories)
    contexto ={
        'categoryForm':categoryForm
    }
    if request.method == 'POST':
        categoryForm = forms.CategoryForm(request.POST, instance=categories)
        if categoryForm.is_valid():
            category=categoryForm.save()
            category.save()
            return redirect('admin-view-category')
    return render(request, 'quiz/update_category.html', contexto)

@login_required(login_url='adminlogin')
def delete_category_view(request,pk):
    category=models.Category.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect('/admin-view-category')