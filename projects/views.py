from django.shortcuts import render,redirect
from .models import * 
from .forms import ProjectForm
# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):

    projects= Project.objects.all() 

    
  

    context = {'name':'methun' , 'id':1 , 'project':projects }
    return render(request , 'projects/projects.html', context)

def project(request,pk):

    project = Project.objects.get(id=pk)
    tags = project.tags.all()

    context = { 'project':project , 'tags':tags } 

    return render(request , 'projects/single-project.html' , context) 



def createProject(request):
   
    form = ProjectForm() 

    if request.method == 'POST':
        
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            # project = form.save(commit=False)
            # project.owner = profile
            form.save()

            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context) 


def updateProject(request, pk):
    project  = Project.objects.get(id=pk) 
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        

        form = ProjectForm(request.POST, request.FILES,instance=project)
        if form.is_valid():
           form.save()

           return redirect('projects')

    context = {'form': form, 'project': project}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
   
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)