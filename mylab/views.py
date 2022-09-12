from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm, PatientsForm, AnalysisForm, CollectorsForm, MedicalsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Prescription, Analysis, Collectors, Medicals, Doctor
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView


@login_required(login_url='/login')
def home(request):
    prescription =  Prescription.objects.all()
    doctor = Doctor.objects.all()

    doctor_count = doctor.count()

    total_patients = prescription.count()
    prescription_count = prescription.count()

    context = {'total_patients':total_patients, 'prescription_count':prescription_count, 'doctor_count':doctor_count, 'prescription': prescription}

    return render(request, 'dashboard/home.html', context)


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})

########################## PRESCRIPTION #####################################################
class PatientsList(ListView):
    models = Prescription
    template_name = 'dashboard/prescription_list.html'

    def get_queryset(self):
        return Prescription.objects.all()


class PatientView(CreateView):
    template_name = 'dashboard/prescription_form.html'
    form_class = PatientsForm
    success_url = '/list'
    

def patient_update(request, id):
    prescription = Prescription.objects.get(id=id)

    if request.method == 'POST':
        form = PatientsForm(request.POST, instance=prescription)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            messages.success(request, 'Form Updated Successfully')
            # redirect to the detail page of the `Band` we just updated
            return redirect('/list', prescription.id)
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = PatientsForm(instance=prescription)
    
    return render(request,'dashboard/prescription_form.html', {'form': form})
    


def patients_delete(request, id):
    prescription = Prescription.objects.get(pk=id)
    prescription.delete()
    return redirect('/list')

########################## END PRESCRIPTION #####################################################

########################## Analyse #####################################################
def analysis_list(request):
    context = {'analysis_list': Analysis.objects.all()}
    return render(request, 'dashboard/analysis_list.html', context)


def analysis_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = AnalysisForm()
        else:
            analysis = Analysis.objects.get(pk=id)
            form = AnalysisForm(instance=analysis)
        return render(request, 'dashboard/analysis_form.html', {'form': form})
    else:
        if id == 0:
            form = AnalysisForm(request.POST)
        else:
            analysis = Analysis.objects.get(pk=id)
            form = AnalysisForm(request.POST, instance=analysis)
        if form.is_valid():
            form.save()
        return redirect('/alist')

def analysis_delete(request,id):
    analysis = Analysis.objects.get(pk=id)
    analysis.delete()
    return redirect('/alist')
########################## End Analyse #####################################################

########################## Collectors #####################################################
def collectors_list(request):
    context = {'collectors_list': Collectors.objects.all()}
    return render(request, 'dashboard/collectors_list.html', context)


def collectors_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            cform = CollectorsForm()
        else:
            collectors = Collectors.objects.get(pk=id)
            cform = CollectorsForm(instance=collectors)
        return render(request, 'dashboard/collectors_form.html', {'cform': cform})
    else:
        if id == 0:
            cform = CollectorsForm(request.POST)
        else:
            collectors = Collectors.objects.get(pk=id)
            cform = CollectorsForm(request.POST, instance=collectors)
        if cform.is_valid():
            cform.save()
        return redirect('/clist')

def collectors_delete(request,id):
    collectors = Collectors.objects.get(pk=id)
    collectors.delete()
    return redirect('/clist')
########################## End Collectors #####################################################

########################## Medicals #####################################################
def medicals_list(request):
    context = {'medicals_list': Medicals.objects.all()}
    return render(request, 'dashboard/medicals_list.html', context)


def medicals_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            mform = MedicalsForm()
        else:
            medicals = Medicals.objects.get(pk=id)
            mform = MedicalsForm(instance=medicals)
        return render(request, 'dashboard/medicals_form.html', {'mform': mform})
    else:
        if id == 0:
            mform = MedicalsForm(request.POST)
        else:
            medicals = Medicals.objects.get(pk=id)
            mform = MedicalsForm(request.POST, instance=medicals)
        if mform.is_valid():
            mform.save()
        return redirect('/mlist')

def medicals_delete(request,id):
    medicals = Medicals.objects.get(pk=id)
    medicals.delete()
    return redirect('/mlist')
########################## End Medicals #####################################################