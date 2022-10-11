import django_filters

from .models import *

class PrescriptionFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['id', 'emp_id', 'doctor', 'occupation', 'address', 'town', 'status', 'telephone1', 'telephone2', 'marital_status', 'gender', 'dob', 'date_added' ]