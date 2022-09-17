from django.urls import path
from . import views
from .views import PatientView, PatientsList
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign_up', views.sign_up, name='sign_up'),

########################## PRESCRIPTION #####################################################
    path('form', PatientView.as_view(), name='patients_form'),
    path('list', PatientsList.as_view(), name='patients_list'),
    path('update_patient/<str:id>/', views.patient_update, name="update_patient"),
    path('patients_delete/<str:id>/', views.patients_delete, name="patients_delete"),
########################## END PRESCRIPTION #####################################################

########################## Collectors #####################################################
    path('cform', views.collectors_form, name='collectors_form'),
    path('clist', views.collectors_list, name='collectors_list'),
    path('update_collectors/<str:id>/', views.collectors_form, name="update_collectors"),
    path('collectors_delete/<str:id>/', views.collectors_delete, name="collectors_delete"),
########################## End Collectors #####################################################

########################## Medicals #####################################################
    path('mform', views.medicals_form, name='medicals_form'),
    path('mlist', views.medicals_list, name='medicals_list'),
    path('update_medicals/<str:id>/', views.medicals_form, name="update_medicals"),
    path('medicals_delete/<str:id>/', views.medicals_delete, name="medicals_delete"),
########################## End Medicals #####################################################
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),

    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]