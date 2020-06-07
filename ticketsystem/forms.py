from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import VehicleCompany, Vehicle, Reservation, SeatPlan

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        #exclude=['vehicleowner']
        widgets={
            'departuretime':forms.TextInput(attrs={'placeholder':'HH:MM:SS'}),
            'boardingpointone':forms.TextInput(attrs={'required': False}),
            
        }  



class CreateVendorForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


class CompanyprofileForm(ModelForm):
    companylogo = forms.ImageField(required=False)
    class Meta:
        model = VehicleCompany
        fields = ['company_name', 'authorizedperson', 'address', 'phone','companylogo', 'company_info', 'slug']
        # widgets={
        #     'company_info':TinyMCE(attrs={'class':'form-control'}),
        # }


class ReservationForm(ModelForm):
    
    class Meta:
        model = Reservation
        fields = '__all__'
        #fields = ['id','fullname','address','email','phone','busid','busName','departurefrom','departureto','departuredate','departuretime','seatnumber','totalprice','paymentmode']
        widgets={
            'departuredate':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'departuretime':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'seatnumber':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'totalprice':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
        }   


class SeatPlanForm(ModelForm):
    class Meta:
        model = SeatPlan
        fields = '__all__'
        
        