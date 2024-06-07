from .models import StudentData
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = "__all__"