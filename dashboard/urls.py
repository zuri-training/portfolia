from django.urls import path
from . import views


# URLConf
urlpatterns =[
    path('dashboard/', views.index, name="dashboard"),
]