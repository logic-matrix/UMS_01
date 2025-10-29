from django.contrib import admin
 
from student.models import Students
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','email',)

 
 
 
