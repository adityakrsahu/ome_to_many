from django.contrib import admin
from .models import StudentModel, DepartmentModel
# Register your models here.

class Department(admin.ModelAdmin):
    list_display = ['id','dep_name','description']
admin.site.register(DepartmentModel,Department)

class Student(admin.ModelAdmin):
    list_display = ['id','stu_name','stu_class','stu_email','stu_mobile','stu_department']
admin.site.register(StudentModel,Student)