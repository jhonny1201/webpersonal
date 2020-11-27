from django.shortcuts import render, get_object_or_404
from .models import Projects

# Create your views here.

def view_portfolio(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_detail(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    context = {
    'project':project
    }   
    return render(request, 'portfolio/portfolio_detail.html', context)