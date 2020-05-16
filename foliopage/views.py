from django.shortcuts import render
from django.views import View
from .models import Project, Person, Skill, Experience

# Create your views here.
def index(request):
    projects_list = Project.objects.order_by('priority')
    person = Person.objects.all()
    skill = Skill.objects.all()
    experience = Experience.objects.all()
    context = {
        'projects_list': projects_list,
        'person': person,
        'skill': skill,
        'experience': experience,
    }
    return render(request, 'index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)