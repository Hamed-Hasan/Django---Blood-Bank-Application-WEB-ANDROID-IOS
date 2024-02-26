
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')), # ✔️☑️✅
    path('donor_profiles/', include('donor_profiles.urls')), # ✔️☑️✅
    path('events/', include('events.urls')), # waiting
    path('donation_history/', include('donation_history.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)