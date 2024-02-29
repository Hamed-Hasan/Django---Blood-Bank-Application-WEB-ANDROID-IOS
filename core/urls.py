

from django.urls import path,include
from . import views
from .views import home

urlpatterns = [
    path('', views.home,name="home" ),
    path('<slug:book_model_slug>/', home, name='home'), 
]
