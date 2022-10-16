from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column



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
        exclude = {'uniqueId', 'slug', 'date_created', 'last_updated'}
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
###############################################################################################3
class ResultsForm(forms.ModelForm):
    THE_OPTIONS = [
    ('Mouffo Michael', 'Mouffo Michael'),
    ('Mandeng Grace', 'Mandeng Grace'),
    ('Mary Jane', 'Mary Jane'),
    ('Suh Samuel', 'Suh Samuel'),
    ]


    STATUS_OPTIONS = [
    ('CURRENT', 'CURRENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = forms.CharField(
                    required = True,
                    label='Result Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Result Title'}),)

    paymentTerms = forms.ChoiceField(
                    choices = THE_OPTIONS,
                    required = False,
                    label='Select Doctor In Charge',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Change Result Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    notes = forms.CharField(
                    required = True,
                    label='Enter Patient results',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    dueDate = forms.DateField(
                    required = True,
                    label='Result Due',
                    widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('dueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('paymentTerms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notes',

            Submit('submit', ' UPDATE RESULTS '))

    class Meta:
        model = Results
        fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['clientName', 'clientLogo', 'addressLine1', 'province', 'postalCode', 'phoneNumber', 'emailAddress', 'taxNumber']

class PatientSelectForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        self.initial_patient = kwargs.pop('initial_patient')
        self.PATIENT_LIST = Prescription.objects.all()
        self.PATIENT_CHOICES = [('-----', '--Select a Patient--')]


        for prescription in self.PATIENT_LIST:
            d_t = (prescription.uniqueId, prescription.first_name)
            self.PATIENT_CHOICES.append(d_t)


        super(PatientSelectForm,self).__init__(*args,**kwargs)

        self.fields['prescription'] = forms.ChoiceField(
                                        label='Choose a related patient',
                                        choices = self.PATIENT_CHOICES,
                                        widget=forms.Select(attrs={'class': 'form-control mb-3'}),)

    class Meta:
        model = Results
        fields = ['prescription']

    def clean_prescription(self):
        c_prescription = self.cleaned_data['prescription']
        if c_prescription == '':
            return None
        else:
            return Prescription.objects.get(uniqueId=c_prescription)

class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['uniqueId', 'slug', 'date_created', 'last_updated']