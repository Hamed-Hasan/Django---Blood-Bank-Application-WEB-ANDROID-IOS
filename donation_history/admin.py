from django.contrib import admin
from .models import DonationHistory

@admin.register(DonationHistory)
class DonationHistoryAdmin(admin.ModelAdmin):
    list_display = ('donor', 'recipient', 'event', 'status')
    list_filter = ('status',)
    search_fields = ('donor__username', 'recipient__username', 'event__title')
