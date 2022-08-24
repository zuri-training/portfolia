from django.shortcuts import render

# Create your views here.

def template_gallery_view(request):
    return render(request, 'template-gallery.html')

def template_london_both(request):
    return render(request, 'london_broth.html')
    
def template_junemung(request):
    return render(request, 'junemung.html')