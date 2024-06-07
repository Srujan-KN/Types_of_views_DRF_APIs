from django.db import models

# Create your models here.

class StudentData(models.Model):
    srn = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    

    class Meta:
        db_table = 'student_data'

