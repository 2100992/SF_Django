from django import forms
from my_first_aid_kit.models import Medicament

class MedicamentForm(forms.ModelForm):
    class Meta:
        model = Medicament
        fields = '__all__'