from django.urls import path
from .views import documentation_view, about_view, homepage_view

app_name = "pages"
urlpatterns =[
    path('documentation/', documentation_view, name="documentation"),
    path('home/', homepage_view, name="home"),
    path('about/', about_view, name="about"),

]