from django.urls import path
from user import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('userclick', views.userclick_view),
    path('userlogin', LoginView.as_view(template_name='user/userlogin.html'),name='userlogin'),
    path('usersignup', views.user_signup_view,name='usersignup'),

    path('user-dashboard', views.user_dashboard_view,name='user-dashboard'),
    path('edit-profile', views.edit_profile, name = 'edit-profile'),
    path('user-exam', views.user_exam_view,name='user-exam'),



    path('calculate-marks', views.calculate_marks_view,name='calculate-marks'),
    path('view-result', views.view_result_view,name='view-result'),
    path('check-marks/<int:pk>', views.check_marks_view,name='check-marks'),
    path('user-marks', views.user_marks_view,name='user-marks'),
    path('user-ranking', views.ranking, name='ranking'),
]