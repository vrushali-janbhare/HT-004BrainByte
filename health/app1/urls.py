from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('reg/', views.reg, name='reg'),
      path('login/', views.user_login, name='login'),
      path('doctor/', views.doctor_panel, name='doctor_panel'),
      path('complete/<int:id>/', views.mark_completed, name='mark_completed'),
      path('skip/<int:id>/', views.skip_patient, name='skip_patient'),
      path('emergency/<int:id>/', views.emergency_patient, name='emergency_patient'),

       
]


