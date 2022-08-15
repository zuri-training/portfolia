from django.urls import path
from . import views


# URLConf
urlpatterns =[
    path('dashboard/<str:pk>', views.index, name="dashboard"),
]