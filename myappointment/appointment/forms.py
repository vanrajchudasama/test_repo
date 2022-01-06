from django import forms
from .models import Appointment
import arrow
from django.core.exceptions import ValidationError  
class AppointmentForm(forms.ModelForm):

    name = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label='Phone Number',widget=forms.NumberInput(attrs={'class':'form-control'}))
    time = forms.CharField(label='Time',widget=forms.TimeInput(attrs={'class':'form-control'}))

    
    class Meta:
        model=Appointment
        fields = '__all__'
    # def clean(self):
    #     """Checks that appointments are not scheduled in the past"""

    #     appointment_time = arrow.get(self.time, self.time_zone.zone)
    #     print(appointment_time,' = = ',arrow.utcnow())
    #     if appointment_time < arrow.utcnow():
    #         raise ValidationError(
    #             'You cannot schedule an appointment for the past. '
    #             'Please check your time and time_zone')