from django.urls import path
from user import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('userclick', views.userclick_view),
    path('userlogin', LoginView.as_view(template_name='user/userlogin.html'),name='userlogin'),
    path('usersignup', views.user_signup_view,name='usersignup'),
]