from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView

from .models import Patient,Owner
from .forms import OwnerForm,PatientForm

# Create your views here.
def home(request):
  return render(request,'vetoffice/home.html')

class OwnerList(ListView):
  model = Owner
  template_name = 'vetoffice/owner_list.html'

class OwnerCreate(CreateView):
  model = Owner
  template_name = 'vetoffice/owner_create_form.html'
  form_class = OwnerForm

class OwnerUpdate(UpdateView):
  model = Owner
  template_name = 'vetoffice/owner_update_form.html'
  form_class = OwnerForm


class OwnerDelete(DeleteView):
  model = Owner
  template_name = 'vetoffice/owner_delete_form.html' 
  success_url = '/owner/list'


class PatientList(ListView):
  model = Patient
  template_name = 'vetoffice/patient_list.html'


class PatientCreate(CreateView):
  model = Patient
  template_name = 'vetoffice/patient_create_form.html'  
  form_class = PatientForm

class PatientUpdate(UpdateView):
  model = Patient
  template_name = 'vetoffice/patient_update_form.html'
  form_class = PatientForm

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'vetoffice/patient_delete_form.html' 
    success_url = '/patient/list'
