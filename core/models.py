from django.db import models
# Create your models here.
from django.db import models
 
#########################################################################
class Student(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
        ('super_admin', 'Super Admin'),
    )

    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.name} ({self.role})"
    

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    course_description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.course_name
    


#########################################################################
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name