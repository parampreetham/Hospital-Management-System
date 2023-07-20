from django import forms
from django.forms import ModelForm
from .models import students,visitors,hostels

class studentForm(ModelForm):
    class Meta:
        model = students
        fields = '__all__'  #('fname','lname','phone','dept','jyear','room_no')
       

class visitorsForm(ModelForm):
    class Meta:
        model = visitors
        fields = '__all__'

class hostelForm(ModelForm):
    class Meta:
        model=hostels
        fields= '__all__'

        labels={
            'name':'',
            'image':'',
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'image':forms.FileInput(attrs={'class':'form-control','accept':'image/*'})
        }