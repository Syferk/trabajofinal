
from django import forms
from django.contrib.auth.models import User
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name','question_number']

class QuestionForm(forms.ModelForm):
    categoryID=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Nombre de categoría", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['question','option1','option2','option3','option4','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }

