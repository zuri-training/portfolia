from django.shortcuts import render

# Create your views here.

def template_gallery_view(request):
    return render(request, 'template-gallery.html')