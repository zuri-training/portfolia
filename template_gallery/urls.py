from django.urls import path
from .views import template_gallery_view, template_london_both, template_junemung


app_name = "template_gallery"
urlpatterns =[
    path('template_gallery/', template_gallery_view, name="template_gallery"),
    path('template_gallery/london_broth', template_london_both, name="london_broth"),
    path('template_gallery/junemung', template_junemung, name="junemung"),
]