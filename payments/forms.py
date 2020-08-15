from django import forms
from . models import invoice,dbupdate


class invoiceform(forms.Form):
    invoicenumber = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'on','pattern':'[0-9a-zA-Z]+', 'title':'Only alphanumeric characters are allowed.'}))
    clientname = forms.CharField(widget=forms.TextInput())
    clientemailid = forms.EmailField(widget=forms.EmailInput())
    projectname = forms.CharField(widget=forms.TextInput())
    amounttobecharged=forms.IntegerField(widget=forms.NumberInput())
class invoicedata(forms.Form):
    yourinvoice = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'on','pattern':'[0-9a-zA-Z]+', 'title':'Only alphanumeric characters are allowed.'}))

