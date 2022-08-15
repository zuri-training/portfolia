from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


# Create your views here.
User = get_user_model()

def documentation_view(request):
    return render(request, 'welcome.html')


def about_view(request):
    return render(request, 'about-us.html')

@login_required
def homepage_view(request):
    return render(request, 'home.html')