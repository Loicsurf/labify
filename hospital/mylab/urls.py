from django.urls import path
from . import views
from .views import PatientView, PatientsList


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

########################## Analyse #####################################################
    path('aform', views.analysis_form, name='analysis_form'),
    path('alist', views.analysis_list, name='analysis_list'),
    path('update_analysis/<str:id>/', views.analysis_form, name="update_analysis"),
    path('analysis_delete/<str:id>/', views.analysis_delete, name="analysis_delete"),
########################## END ANALYSE #####################################################

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

]