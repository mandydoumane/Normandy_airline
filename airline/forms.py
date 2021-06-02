from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import *
from datetime import date, datetime

    
# class User_info(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'


CABIN_CHOICES = [
    ('1', 'First Class'),
    ('2', 'Business Class'),
    ('3', 'Economy Class'),
]
gender_CHOICES = [
    ('1', 'MR'),
    ('2', 'Mme'),
]
        
class Pageone(forms.Form):
    departure = forms.ModelChoiceField(queryset=Airport.objects.all())
    arrival = forms.ModelChoiceField(queryset=Airport.objects.all())
    date = forms.DateField(widget = forms.DateInput(attrs={'type':'date', 'class':'datepicker'}))
   
    class Meta:
        model = Flight
        fields = [
            'departure',
            'arrival',
            'date',
        ]
        
class PageTwo(forms.Form):
    gender = forms.ChoiceField(choices=gender_CHOICES)
    first_name = forms.CharField()
    last_name = forms.CharField()
    date_birth = forms.DateField(widget = forms.DateInput(attrs={'type':'date', 'class':'datepicker'}))
    email = forms.EmailField()
    