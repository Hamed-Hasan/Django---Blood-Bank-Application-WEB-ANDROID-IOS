

from django.urls import path

from core.views import home
from . import views


urlpatterns = [
   
    path('filter/<slug:book_model_slug>/', home,name="books_filter" ),
    path('purchase/<int:id>/', views.purchased_view,name="purchase" ),
    path('purchase/history/', views.purchase_history,name="purchase_history" ),
    # path('details/<int:id>/', views.BookDetailsView.as_view(),name="details" ),
    path('details/<int:id>/', views.books_details,name="details" ),
    path('return/<int:id>/', views.return_book,name="return" ),
    
]
