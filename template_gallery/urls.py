from django.urls import path
from .views import template_gallery_view

urlpatterns =[
    path('template_gallery/', template_gallery_view, name="template_gallery"),
]