from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='myapp-home'),
    path('about/', views.about, name='myapp-about'),
]
