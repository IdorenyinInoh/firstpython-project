from django.db import models

# Create your models here.

class Student(models.Model):
    COURSES = [
        ('AI', 'Professional Diploma in Artificial Intelligence'),
        ('IT', 'Professional Diploma in Data Analytics'),
        ('ECE', 'Professional Diploma in Software Engineering'),
        ('ME', 'Professional Diploma in Blockchain Technology'),
    ] 

    student_Id = models.CharField(max_length=150, unique=True)
    names = models.CharField(max_length=150)
    course = models.CharField(max_length=10, choices=COURSES)
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=False, null=True, blank=True)

    def _str_(self):
        return self.names

class Attendance(models.Model):
    studentId = models.CharField(max_length=100, unique=False)
    date = models.DateTimeField(unique=True)
    studentName = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.studentId
