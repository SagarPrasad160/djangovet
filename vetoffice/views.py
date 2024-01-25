from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import UpdateView,CreateView,DeleteView

from .models import Patient,Owner
from .forms import PatientCreateForm,OwnerCreateForm

# Create your views here.
def home(request):
  return render(request,'vetoffice/home.html')

class OwnerList(ListView):
  model = Owner
  template_name = 'vetoffice/owner_list.html'

class OwnerCreate(CreateView):
  model = Owner
  template_name = 'vetoffice/owner_create_form.html'
  form_class =OwnerCreateForm


class PatientList(ListView):
  model = Patient
  template_name = 'vetoffice/patient_list.html'


class PatientCreate(CreateView):
  model = Patient
  template_name = 'vetoffice/patient_create_form.html'  
  form_class = PatientCreateForm
