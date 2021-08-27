from django.db import models

from user.models import User
class Category(models.Model):
   category_name = models.CharField(max_length=50)
   question_available = models.PositiveIntegerField(default=0)
   question_number = models.PositiveIntegerField()
   def __str__(self):
        return self.category_name

class Question(models.Model):
    course=models.ForeignKey(Category,on_delete=models.CASCADE)
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    exam = models.ForeignKey(Category,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    correct = models.PositiveIntegerField(default= 0)
    total_questions = models.PositiveIntegerField(default= 0)

