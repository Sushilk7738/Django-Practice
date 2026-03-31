from django.contrib import admin
from testapp.models import Student, Employee

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["rollno", "name", "marks", "address"]
admin.site.register(Student, StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_id", "name", "department", "salary"]
admin.site.register(Employee,EmployeeAdmin)