
from django.urls import path
from . import views

urlpatterns = [
    
    path('signup', views.signup,name='signup'),
    path('login/', views.User_login,name='loginpage'),
    # path('login/', views.UserLoginViewClass.as_view(),name='loginpage'),
    path('logout/', views.user_logout,name='user_logout'),
    path('pass_change/', views.change_pass,name='change_pass'),
    path('pass_change2/', views.change_pass2,name='change_pass2'),
    path('profile/', views.profile,name='profilepage'),
    path('update/', views.update_profile,name='update_profile'),
    

]
