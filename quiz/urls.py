from django.contrib import admin
from django.urls import path,include
from quiz import views


app_name='quiz'

urlpatterns=[
    path('',views.ChapterListView.as_view(),name='list'),
    path('<int:pk>/',views.QuestionDetailView.as_view(),name='detail'),
    path('create/',views.ChapterCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.QuestionUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.ChapterDeleteView.as_view(),name='delete'),


]
