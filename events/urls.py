

from django.urls import path
from .views import EventCreateAPIView, EventAcceptAPIView, EventDetailAPIView

urlpatterns = [
    path('create/', EventCreateAPIView.as_view(), name='event_create'),
    path('accept/<int:pk>/', EventAcceptAPIView.as_view(), name='event_accept'),
    path('detail/<int:pk>/', EventDetailAPIView.as_view(), name='event_detail'),
]
