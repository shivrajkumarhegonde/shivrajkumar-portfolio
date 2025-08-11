# core/views.py
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
def home(request):
    context = {}
    return render(request, 'core/home.html', context)

def about(request):
    """
    Renders the about page.
    """
    context = {}
    return render(request, 'core/about.html', context)

def skills(request):
    """
    Renders the skills page and passes a dictionary of skills data
    to the template.
    """
    skills_data = {
        'Languages': [
            {'name': 'Python', 'level': 90},
            {'name': 'Java', 'level': 75},
            {'name': 'C++', 'level': 70},
            {'name': 'JavaScript', 'level': 80},
            {'name': 'SQL', 'level': 85},
        ],
        'Frameworks & Libraries': [
            {'name': 'Django', 'level': 85},
            {'name': 'React', 'level': 65},
            {'name': 'Node.js', 'level': 60},
            {'name': 'Bootstrap', 'level': 95},
        ],
        'Databases': [
            {'name': 'MySQL', 'level': 80},
            {'name': 'PostgreSQL', 'level': 70},
            {'name': 'MongoDB', 'level': 65},
        ],
        'Tools & Technologies': [
            {'name': 'Git & GitHub', 'level': 90},
            {'name': 'Docker', 'level': 50},
            {'name': 'REST APIs', 'level': 80},
        ]
    }
    context = {'skills_data': skills_data}
    return render(request, 'core/skills.html', context)

def projects(request):
    """
    Renders the projects page, fetching all projects from the database.
    """
    projects = Project.objects.all().order_by('-date_created') # Get all projects, newest first
    context = {'projects': projects}
    return render(request, 'core/projects.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from: {name} ({from_email})\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,  # <-- CHANGE THIS LINE
                ['shivrajkumar.hegonde_civil21@pccoer.in'],
                fail_silently=False,
            )
            return redirect('/contact/?success=true')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'core/contact.html', context)

def resume(request):
    """
    Renders the resume page.
    """
    return render(request, 'core/resume.html')

class ProjectCreateView(CreateView):
    model = Project
    # These are the fields that will appear on the form
    fields = ['title', 'description', 'technologies', 'image', 'demo_link', 'github_link']
    template_name = 'core/project_form.html'
    # After success, redirect to the main projects page
    success_url = reverse_lazy('projects')

class ProjectUpdateView(UpdateView):
    model = Project
    fields = ['title', 'description', 'technologies', 'image', 'demo_link', 'github_link']
    template_name = 'core/project_form.html' # We reuse the same form template!
    success_url = reverse_lazy('projects')

# Add this new class for deleting projects
class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'core/project_confirm_delete.html' # We need a new template for this
    success_url = reverse_lazy('projects')