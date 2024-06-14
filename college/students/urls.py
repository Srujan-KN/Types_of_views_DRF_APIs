
from django.urls import path
from .views import StudentAPIView

urlpatterns = [
    path('class_based/students/', StudentAPIView.as_view(), name='student_list_create'),
    path('class_based/students/<str:pk>/', StudentAPIView.as_view(), name='student_detail'),
]