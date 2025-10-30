from django.contrib import admin
from django.urls import path
from django.contrib.auth import get_user_model
from core.models import Course, Student
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from django.template.response import TemplateResponse




# Register your models here.
@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','email','role','student_id',)
    #list_filter = ('role',)
    list_per_page = 10
    #search_fields = ('name', 'email','id',)

 
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'course_description',)
    search_fields = ('course_code',)
 


class CustomAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"
    site_title = "Dashboard Admin"
    index_title = "Welcome to the Dashboard"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('', self.admin_view(self.custom_dashboard))
        ]
        return custom_urls + urls

    def custom_dashboard(self, request):
        user_model = get_user_model()
        context = dict(
            self.each_context(request),
            user_count=user_model.objects.count(),
            course_count=Course.objects.count(),
            recent_actions=LogEntry.objects.all().order_by('-action_time')[:5]
        )
        return TemplateResponse(request, "admin/index.html", context)

# Replace default admin site
admin_site = CustomAdminSite(name='custom_admin')
