from django.contrib import admin
from django.urls import path,include
from quiz import views
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),

    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='quiz/index.html'),name='logout'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    
    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='quiz/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
    
    path('admin-user', views.admin_user_view,name='admin-user'),
    path('admin-view-user', views.admin_view_user_view,name='admin-view-user'),
    path('admin-view-user-marks', views.admin_view_user_marks_view,name='admin-view-user-marks'),
    path('admin-view-marks/<int:pk>', views.admin_view_marks_view,name='admin-view-marks'),
    path('admin-view-statistics/<int:pk>', views.admin_view_statistics,name='admin-view-statistics'),
    path('admin-check-marks/<int:pk>', views.admin_check_marks_view,name='admin-check-marks'),
    path('update-user/<int:pk>', views.update_user_view,name='update-user'),
    path('delete-user/<int:pk>', views.delete_user_view,name='delete-user'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('update-category/<int:pk>', views.admin_update_category_view, name='update-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('admin-add-question', views.admin_add_question_view,name='admin-add-question'),
    path('admin-view-question', views.admin_view_question_view,name='admin-view-question'),
    path('view-question/<int:pk>', views.view_question_view,name='view-question'),
    path('update-question/<int:pk>', views.update_question_view, name= 'update-question'),
    path('delete-question/<int:pk>', views.delete_question_view,name='delete-question'),
]
