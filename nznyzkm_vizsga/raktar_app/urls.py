from django.urls import path
from . import views


urlpatterns = [
       
    path('login/', views.bejelentkezes, name ='login'),
    path('logout/', views.logout_page, name='logout'),
    path('',views.home, name = 'home'),
    path('raktar/' ,views.bevitel_kiadas, name='raktar'),
    path('megrendeles/', views.megrendeles, name= 'megrendeles'),
    path('megrendelesnyomtatas/<int:id>/', views.megrendelesnyomtatas, name='megrendelesnyomtatas'),     
       
]   