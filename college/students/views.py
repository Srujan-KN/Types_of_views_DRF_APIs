from rest_framework.decorators import api_view
from .models import StudentData
from rest_framework.response import Response
from .serializers import StudentDataSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


class StudentAPIView(APIView):
    '''
        1. Implementing CRUD APIs using Class based views (APIView)
    '''
    def post(self, request):
        serializer = StudentDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None):
        if pk:
            student = get_object_or_404(StudentData, pk=pk)
            serializer = StudentDataSerializer(student)
            return Response(serializer.data)
        else:
            students = StudentData.objects.all()
            serializer = StudentDataSerializer(students, many=True)
            return Response(serializer.data)

    def put(self, request, pk=None):
        student = get_object_or_404(StudentData, pk=pk)
        serializer = StudentDataSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        student = get_object_or_404(StudentData, pk=pk)
        serializer = StudentDataSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        student = get_object_or_404(StudentData, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_data_api(request, pk=None):
    '''
        2. Implementing CRUD APIs using Function based views (@api_view decorator)
    '''
    if request.method == 'GET':
        if pk:
            try:
                student = StudentData.objects.get(srn=pk)
                serializer = StudentDataSerializer(student)
                return Response(serializer.data)
            except StudentData.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            students = StudentData.objects.all()
            serializer = StudentDataSerializer(students, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        try:
            student = StudentData.objects.get(srn=pk)
        except StudentData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'PUT':
            serializer = StudentDataSerializer(student, data=request.data)
        elif request.method == 'PATCH':
            serializer = StudentDataSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            student = StudentData.objects.get(srn=pk)
        except StudentData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
