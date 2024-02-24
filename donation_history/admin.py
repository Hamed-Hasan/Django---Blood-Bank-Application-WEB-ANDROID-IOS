from django.contrib import admin
from .models import DonationHistory

@admin.register(DonationHistory)
class DonationHistoryAdmin(admin.ModelAdmin):
    list_display = ('donor', 'recipient', 'event', 'status')
