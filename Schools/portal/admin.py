from django.contrib import admin
from .models import Student, Attendance
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['--all--']

class AttendanceAdmin(admin.ModelAdmin):
    search_fields = ['--all--']

admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin) 
