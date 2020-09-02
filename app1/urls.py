from django.urls import path,include
from app1 import views
app_name='app1'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('student/',views.register_student,name='student'),
    path('teacher/',views.register_teacher,name='teacher'),
    path('login/',views.user_login,name='user_login')

]
