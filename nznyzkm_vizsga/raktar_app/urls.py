from django.urls import path
from . import views


urlpatterns = [
       
    path('login/', views.bejelentkezes, name ='login'),
    path('logout/', views.logout_page, name='logout'),
    path('',views.home, name = 'home'),
    path('raktar/' ,views.bevitel_kiadas, name='raktar'),
    path('megrendeles/', views.megrendeles, name= 'megrendeles'),
       
   
    #path('megrendelesek/', HomeView.as_view(), name= 'home'),
    #path('raktar/', RaktarView.as_view(), name= 'raktar'),
    #path('dolgozo/', DolgozoView.as_view(), name= 'dolgozo'),
    #path('',HomeView.as_view(), name = 'home'),
    #path('dolgozo/',views.dolgozo, name = 'dolgozo'),
    #path('bevitel/' ,views.bevitel, name='bevitel')
    
    
]   