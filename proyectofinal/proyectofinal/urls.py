from django.contrib import admin
from django.urls import path,include
from quiz import views
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='quiz/index.html'),name='logout'),
]
