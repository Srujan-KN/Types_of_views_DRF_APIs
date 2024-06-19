
from django.urls import path
from .views import StudentAPIView, student_data_api

urlpatterns = [
    path('class_based/students/', StudentAPIView.as_view(), name='student_list_create'),
    path('class_based/students/<str:pk>/', StudentAPIView.as_view(), name='student_detail'),

    path('func_based/students/', student_data_api, name='student-data-list-create'),
    path('func_based/students/<str:pk>/', student_data_api, name='student-data-detail'),
]