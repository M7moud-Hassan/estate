from django import forms

from imported.models import Imported

class ImportedForm(forms.ModelForm):
    class Meta:
        model = Imported
        fields = '__all__'

    company_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    website=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    