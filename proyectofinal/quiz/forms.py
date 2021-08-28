
from django import forms
from django.contrib.auth.models import User
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name','question_number','total_marks']

