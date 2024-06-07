from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.views import StudentModelViewset, get_list

router = DefaultRouter()
router.register(r'students', StudentModelViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('students_list/', get_list, name='students_list')
]
