from django.urls import path
from . import viewss
urlpatterns = [
  
    path('',views.index,name="index"),
]