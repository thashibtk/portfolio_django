from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):

    resume = Resume.objects.latest('uploaded_at')

    projects = Project.objects.all().order_by('-created_at')[:3]


    if resume:
        resume_url = resume.file.url
    else:
        resume_url = None

    context = {
        'resume_url': resume_url,
        'projects': projects,
    }

    return render(request, 'index.html', context)

def projects(request):
    return render(request, 'projects.html')

def project_details(request):
    return render(request, 'project_details.html')


def contact(request):
    return render(request, 'contact.html')