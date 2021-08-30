from django.db import models

from django.contrib.auth.models import User

class Users(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/user/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True, blank=True)
   
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_username(self):
        return self.user.username 

    @property
    def get_last_login(self):
        return self.user.last_login
    @property
    def get_date_joined(self):
        return self.user.date_joined
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
