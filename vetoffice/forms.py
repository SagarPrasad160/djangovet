from django import forms

from .models import Patient,Owner

class OwnerForm(forms.ModelForm):
  class Meta:
    model = Owner
    fields = "__all__"

class PatientForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = "__all__"

