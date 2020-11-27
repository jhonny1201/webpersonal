from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def about(request):
    return render(request, 'app/about.html')


