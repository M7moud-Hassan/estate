from django import forms
from django.core.exceptions import ValidationError

from .models import Engineers


def validate_graduation_year(value):
    if not str(value).isdigit() or len(str(value)) != 4 or int(value) > 2023:
        raise ValidationError("Enter a valid 4-digit year not exceeding 2023")


class EngineersForm(forms.ModelForm):
    class Meta:
        model = Engineers
        fields = '__all__'

    name = forms.CharField(max_length=200,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    job_title = forms.CharField(max_length=10,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    graduation_year = forms.IntegerField(
        validators=[validate_graduation_year],
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1950,
        max_value=2023
    )
    phone_number = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control','pattern': r'^01[0,1,2,5]\d{8}$'},))
