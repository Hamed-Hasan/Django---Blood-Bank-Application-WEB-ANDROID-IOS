from django.contrib import admin
from .models import DonorProfile

@admin.register(DonorProfile)
class DonorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'address', 'last_donation_date', 'availability', 'blood_group')
