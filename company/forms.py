from django import forms
from .models import Departments,Branches
from django.core.exceptions import ValidationError

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

    def clean(self):
        cleaned_data = self.cleaned_data
        
        if  Departments.objects.filter(name=cleaned_data['name'], dept_branch= cleaned_data['branches']).exists():
             raise ValidationError('department with this name already exists in brnche')
           

        # Always return cleaned_data
        return cleaned_data

class newDepartmentToBrancheForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','maxlength':500}))
    class Meta:
        model = Departments
        fields = ['name','description']
        exclude = ['dept_branch']

    def __init__(self, *args, **kwargs):
        self.related_branch = kwargs.pop('related_branch', None)
        super().__init__(*args, **kwargs)

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     related_branch = self.related_branch
    #     if  Departments.objects.filter(name=cleaned_data['name'], dept_branch= related_branch).exists():
    #         raise ValidationError('department with this name already exists in brnche')
    #     # Always return cleaned_data
    #     return cleaned_data


class editBrancheForm(forms.ModelForm):
    class Meta:
        model = Branches
        fields = ['name','address','phone']

    