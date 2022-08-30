from django.urls import path
from .views import welcome_view, choose_name_view, congratulations_view, your_role_view, website_type_view


app_name = "documentation"

urlpatterns =[
    path('welcome/', welcome_view, name="welcome"),
    path('website_type/', website_type_view, name="website_type"),
    path('choose_name/', choose_name_view, name="choose_name"),
    path('your_role/', your_role_view, name="your_role"),
    path('congratulations/', congratulations_view, name="congratulations"),

]