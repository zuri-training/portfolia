from django.urls import path
from .views import about_view, homepage_view

app_name = "pages"
urlpatterns =[
    path('home/', homepage_view, name="home"),
    path('about/', about_view, name="about"),

]