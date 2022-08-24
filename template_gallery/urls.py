from django.urls import path
from .views import template_gallery_view, template_london_both, template_junemung

urlpatterns =[
    path('template_gallery/', template_gallery_view, name="template_gallery"),
    path('template_gallery/london_broth', template_london_both, name="template_gallery_london_broth"),
    path('template_gallery/junemung', template_junemung, name="template__junemung"),
]