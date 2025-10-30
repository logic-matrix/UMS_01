from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/admin/login/')
def student(request):
    return render(request, 'student/student_dashboard.html')