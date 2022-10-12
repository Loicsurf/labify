from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Prescription, Interval, Measurement, Collectors, Additives, Technique, Medicals


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    laboratory_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'laboratory_name', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'

class PatientsForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }
        widgets = {
            'dob': DateInput(),
        }


class CollectorsForm(forms.ModelForm):

    class Meta:
        model = Collectors
        fields = '__all__'


class MedicalsForm(forms.ModelForm):

    class Meta:
        model = Medicals
        fields = '__all__'

class PatientSearchForm(forms.ModelForm):
   class Meta:
     model = Prescription
     fields = ['first_name', 'last_name', 'town', 'status', 'doctor', 'gender']