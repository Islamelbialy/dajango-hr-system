from django import forms
from .models import Departments,Branches


class newDepartmentForm(forms.ModelForm):

    branches = forms.ModelChoiceField(
        queryset=Branches.objects.all(),
        to_field_name= 'id',
        required=True,  
        widget=forms.Select()
    )
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','maxlength':500}))
    class Meta:
        model = Departments
        fields = ['name','description','branches']