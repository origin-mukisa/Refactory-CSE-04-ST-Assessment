from django import forms
from .models import *

class PlanePassengerForm(forms.ModelForm):
    class Meta:
        model = PlanePassenger
        fields = ['full_name','gender','date_of_birth','nationality','phone_number','email_address','postbox_number','emergency_phone_number','passport_number',  'departure_city','destination_city']

        labels = {
            'full_name':'Full Name',
            'gender':'Gender',
            'date_of_birth': 'Date Of Birth',
            'nationality': 'Nationality',
            'phone_number':'Phone Number',
            'email_address':'Email Address',
            'postbox_number': 'P.O Box Number',
            'emergency_phone_number': 'Emergency Phone Number',
            'passport_number': 'Passport Number',
            
            'departure_city': 'Departure City',
            'destination_city': 'Destination City'
        }
        


        widgets = {
            'full_name':forms.TextInput(attrs={'placeholder':'Enter your full names'}),
            'date_of_birth':forms.DateInput(attrs={'placeholder':'YYYY/MM/DD', 'type':'date'}),
            'nationality':forms.TextInput(attrs={}),
            'phone_number':forms.NumberInput(attrs={}),
            'email_address':forms.EmailInput(attrs={}),
            'postbox_number':forms.TextInput(attrs={}),
            'emergency_phone_number':forms.NumberInput(attrs={}),
            'passport_number':forms.NumberInput(attrs={}),
            
            'departure_city':forms.TextInput(attrs={}),
            'destination_city':forms.TextInput(attrs={})

        }