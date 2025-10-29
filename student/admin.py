from django.contrib import admin

from student.models import Students

# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','email',)
