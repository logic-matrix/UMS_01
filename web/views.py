from django.shortcuts import render


def web(request):
    return render(request, 'web/index.html')


def about(request):
    return  render(request, 'web/about.html')


def career(request):
    return render(request, 'web/career.html')


def contact(request):
    return render(request, 'web/contact.html')

def academic(request):
    return render(request, 'web/academic.html')


def admission(request):
    return render(request, 'web/admission.html')