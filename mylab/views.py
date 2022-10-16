from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.db.models import Q
from django.http import HttpResponse
from .functions import *
from random import randint
from uuid import uuid4
import pdfkit
from django.template.loader import get_template
import os

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
    model = Prescription
    template_name = 'dashboard/patients_list.html'
    queryset = Prescription.objects.all()
    paginate_by: 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(gender__icontains=q) | Q(town__icontains=q)
            )
        else:
            object_list = self.model.objects.all
        return object_list


class PatientView(CreateView):
    template_name = 'dashboard/patients_form.html'
    form_class = PatientsForm
    success_url = '/list'
    

def patient_update(request, id):
    prescription = Prescription.objects.get(pk=id)

    if request.method == 'POST':
        form = PatientsForm(request.POST, instance=prescription)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            messages.success(request, 'Form Updated Successfully')
            # redirect to the detail page of the `Band` we just updated
            return redirect('/list', prescription.uniqueId)
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = PatientsForm(instance=prescription)
    
    return render(request,'dashboard/patients_form.html', {'form': form})
    


def patients_delete(request, slug):
    prescription = Prescription.objects.get(slug=slug)
    prescription.delete()
    return redirect('/list')

########################## END PRESCRIPTION #####################################################

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

def results(request):
    context = {}
    results = Results.objects.all()
    context['results'] = results

    return render(request, 'dashboard/results.html', context)



def createResults(request):
    #create a blank Results ....
    number = 'Patient-'+str(uuid4()).split('-')[1]
    newResults = Results.objects.create(number=number)
    newResults.save()

    inv = Results.objects.get(number=number)
    return redirect('create-build-results', slug=inv.slug)

def createBuildResults(request, slug):
    #fetch that Results
    try:
        results = Results.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('results')

    #fetch all the doctor - related to this Results
    doctor = Doctor.objects.filter(results=results)


    context = {}
    context['results'] = results
    context['doctor'] = doctor

    if request.method == 'GET':
        doc_form  = DoctorForm()
        inv_form = ResultsForm(instance=results)
        patients_form = PatientSelectForm(initial_patient=results.prescription)
        context['doc_form'] = doc_form
        context['inv_form'] = inv_form
        context['patients_form'] = patients_form
        return render(request, 'dashboard/create-results.html', context)

    if request.method == 'POST':
        doc_form  = DoctorForm(request.POST)
        inv_form = ResultsForm(request.POST, instance=results)
        patients_form = PatientSelectForm(request.POST, initial_patient=results.prescription, instance=results)

        if doc_form.is_valid():
            obj = doc_form.save(commit=False)
            obj.results = results
            obj.save()

            messages.success(request, "Results Doctor added succesfully")
            return redirect('create-build-results', slug=slug)

        elif inv_form.is_valid and 'paymentTerms' in request.POST:
            inv_form.save()

            messages.success(request, "Results updated succesfully")
            return redirect('create-build-results', slug=slug)

        elif patients_form.is_valid() and 'prescription' in request.POST:
            patients_form.save()
            messages.success(request, "Client added to Results succesfully")
            return redirect('create-build-results', slug=slug)
        else:
            context['doc_form'] = doc_form
            context['inv_form'] = inv_form
            context['patients_form'] = patients_form
            messages.error(request,"Problem processing your request")
            return render(request, 'dashboard/create-results.html', context)


    return render(request, 'dashboard/create-results.html', context)


def viewPDFResults(request, slug):
    #fetch that Results
    try:
        results = Results.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('results')

    #fetch all the doctor - related to this Results
    doctor = Doctor.objects.filter(results=results)

    # #Get Client Settings
    p_settings = Settings.objects.filter(clientName='loicsurf')



    context = {}
    context['results'] = results
    context['doctor'] = doctor
    context['p_settings'] = p_settings

    return render(request, 'dashboard/results-template.html', context)

def viewDocumentResults(request, slug):
    #fetch that Results
    try:
        results = Results.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('results')

    #fetch all the doctor - related to this Results
    doctor = Doctor.objects.filter(results=results)

    #Get Client Settings
    p_settings = Settings.objects.filter(clientName='loicsurf')




    context = {}
    context['results'] = results
    context['doctor'] = doctor
    context['p_settings'] = p_settings

    #The name of your PDF file
    filename = '{}.pdf'.format(results.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('dashboard/pdf-template.html')


    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'10', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
      #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    #IF you have CSS to add to template
    css1 = os.path.join(settings.CSS_LOCATION, 'assets', 'css', 'bootstrap.min.css')
    css2 = os.path.join(settings.CSS_LOCATION, 'assets', 'css', 'dashboard.css')

    #Create the file
    file_content = pdfkit.from_string(html, False, configuration=config, options=options)

    #Create the HTTP Response
    response = HttpResponse(file_content, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename = {}'.format(filename)

    #Return
    return response

def emailDocumentResults(request, slug):
    #fetch that Results
    try:
        results = Results.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('results')

    #fetch all the doctor - related to this Results
    doctor = Doctor.objects.filter(results=results)

    #Get Client Settings
    p_settings = Settings.objects.filter(clientName='loicsurf')



    context = {}
    context['results'] = results
    context['doctor'] = doctor
    context['p_settings'] = p_settings

    #The name of your PDF file
    filename = '{}.pdf'.format(results.uniqueId)

    #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('dashboard/pdf-template.html')


    #Render the HTML
    html = template.render(context)

    #Options - Very Important [Don't forget this]
    options = {
          'encoding': 'UTF-8',
          'javascript-delay':'1000', #Optional
          'enable-local-file-access': None, #To be able to access CSS
          'page-size': 'A4',
          'custom-header' : [
              ('Accept-Encoding', 'gzip')
          ],
      }
      #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')

    #Saving the File
    filepath = os.path.join(settings.MEDIA_ROOT, 'patient_results')
    os.makedirs(filepath, exist_ok=True)
    pdf_save_path = filepath+filename
    #Save the PDF
    pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)


    #send the emails to client
    to_email = results.prescription.emailAddress
    from_client = Settings.objects.filter(clientName='loicsurf')
    # from_client = p_settings.clientName
    emailResultsPatient(to_email, from_client, pdf_save_path)

    results.status = 'EMAIL_SENT'
    results.save()

    #Email was send, redirect back to view - Results
    messages.success(request, "Email sent to the client succesfully")
    return redirect('create-build-results', slug=slug)


def deleteResults(request, slug):
    try:
        Results.objects.get(slug=slug).delete()
    except:
        messages.error(request, 'Something went wrong')
        return redirect('results')

    return redirect('results')

def doctor(request):
    context = Doctor.objects.all()
    context['doctor'] = doctor

    return render(request, 'dashboard/results-template.html', context)