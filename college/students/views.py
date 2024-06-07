from .models import StudentData
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import StudentSerializer

class StudentModelViewset(viewsets.ModelViewSet):
    queryset = StudentData.objects.all()
    serializer_class = StudentSerializer


@api_view(["GET"])
def get_list(request):
    print(StudentData.objects.all())
    return Response({})


