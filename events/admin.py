from django.contrib import admin
from .models import Event, EventAcceptance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'blood_group', 'creator')

@admin.register(EventAcceptance)
class EventAcceptanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'accepted_at')
