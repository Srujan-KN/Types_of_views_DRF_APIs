from .models import StudentData
from rest_framework import serializers

class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = "__all__"

        