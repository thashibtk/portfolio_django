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

from django.core.paginator import Paginator

def projects(request):
    project_list = Project.objects.all().order_by('-created_at')
    paginator = Paginator(project_list, 6)  # Show 6 projects per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'projects.html', context)

def project_details(request, slug):

    project = Project.objects.get(slug=slug)

    context = {
        'project': project,
    }

    return render(request, 'project_details.html', context)


from django.shortcuts import render, redirect
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if full_name and email and phone and subject and message:
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message. I will get back to you soon!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill all the fields properly.')

    return render(request, 'contact.html')


