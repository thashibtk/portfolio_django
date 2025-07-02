from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def project_details(request):
    return render(request, 'project_details.html')


def contact(request):
    return render(request, 'contact.html')