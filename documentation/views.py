from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def welcome_view(request):
    return render(request, 'welcome.html')

def website_type_view(request):
    return render(request, 'website_type.html')

def your_role_view(request):
    return render(request, 'your_role.html')

def choose_name_view(request):
    return render(request, 'chose_name.html')

def congratulations_view(request):
    return render(request, 'congratulations.html')
