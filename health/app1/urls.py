from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
      path('login/', views.user_login, name='login'),
      path('doctor/', views.doctor_panel, name='doctor_panel'),
      
      
    
      path('', views.book_appointment, name='book'),
 
]


