
from django.urls import path
from . import views
from . views import depositeMoneyView,transactionCreateMixin

urlpatterns = [
    
    path('deposite/', depositeMoneyView.as_view(),name='deposite'),
    
    

]
