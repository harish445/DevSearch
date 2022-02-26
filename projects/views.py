from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {
        'id' : '1',
        'title': "Ecom website",
        'description': "fully website"
    },
    {
        'id' : '2',
        'title': "portfolio website",
        'description': "fully website"
    },
    {
        'id' : '3',
        'title': "social website",
        'description': "fully website"
    }
]

def projects(request):
    page = 'Home'
    number = 11
    context = {'page': page, 'number': number, 'projects':projectList}
    
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project':projectObj})

sdkfjbs