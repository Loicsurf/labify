from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Prescription, Analysis, Interval, Measurement, Collectors, Additives, Technique, Medicals


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    laboratory_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name',
                  'laboratory_name', 'password1', 'password2']


class PatientsForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name'
        }

class AnalysisForm(forms.ModelForm):

    class Meta:
        model = Analysis
        fields = '__all__'


class CollectorsForm(forms.ModelForm):

    class Meta:
        model = Collectors
        fields = '__all__'


class MedicalsForm(forms.ModelForm):

    class Meta:
        model = Medicals
        fields = '__all__'