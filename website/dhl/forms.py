from django import forms
from .models import BrokerUser,Order
from . import fields

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderId','senderId','premiumUser','packageImage','user','status']

class BrokerUserForm(forms.ModelForm):
    class Meta:
        model = BrokerUser
        fields = ['name','email']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not 'user' in name:
            raise forms.ValidationError("Use user prefix")
        return name
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise forms.ValidationError('Not valid email')
        return email

class NewUserForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    userType = forms.ChoiceField(choices=fields.STATUS_CHOICES,
                                 label='',
                                 initial='1',
                                 widget=forms.Select(),
                                 required=True)