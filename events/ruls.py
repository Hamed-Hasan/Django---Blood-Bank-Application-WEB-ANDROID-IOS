from django.urls import path
from .views import EventCreateAPIView, EventAcceptAPIView

urlpatterns = [
    path('create/', EventCreateAPIView.as_view(), name='event_create'),
    path('accept/<int:pk>/', EventAcceptAPIView.as_view(), name='event_accept'),
]
