from django.contrib import admin
from testapp.models import Employee
from testapp.models import Student

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id" , "ename", "esal", "age"]
admin.site.register(Employee, EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "age", "stream"]
admin.site.register(Student, StudentAdmin)

