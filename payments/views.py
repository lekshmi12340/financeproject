from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import stripe
from django.core.mail import send_mail
from payments.forms import invoiceform
from payments.models import invoice
from django.views.generic.base import TemplateView

def invoicedata(request):
    form = invoiceform()
    if request.method=="POST":
        form=invoiceform(request.POST)
        if form.is_valid():
            invoicenumber = form.cleaned_data['invoicenumber']
            clientname = form.cleaned_data['clientname']
            clientemailid = form.cleaned_data['clientemailid']
            projectname = form.cleaned_data['projectname']
            amounttobecharged = form.cleaned_data['amounttobecharged']
            obj=invoice()
            obj.invoicenumber=invoicenumber
            obj.clientname=clientname
            obj.clientemailid=clientemailid
            obj.projectname=projectname
            obj.amounttobecharged=amounttobecharged
            obj.save()
            return render(request,'payments/datasubmission.html')
    return render(request,'payments/invoice.html',{"form":form})
def generatedinvoice(request):
    if request.method == "POST":
        clientname=request.POST.get("clientname")
        userdata=invoice.objects.filter(clientname=clientname)
        if userdata:
            form = invoiceform()
            return render(request,'payments/invoiceletter.html',{'userdata':userdata})
    return render(request, 'payments/invoicename.html')


class home(TemplateView):
    template_name = 'payments/home.html'


    def get_context_data(self,**kwargs):  # new
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
def charge(request):

   return render(request, 'payments/charge.html')

def emailConsole(request):
    send_mail('Your Invoice','http://127.0.0.1:8000/payments/generatedinvoice','saj.lakshmi@gmail.com',['saj.lakshmi@gmail.com'],fail_silently=False)
    return HttpResponse('successfully send the mail')
def dbupdated(request):
    return render(request,'payments/datasubmission.html')
def clientfilter(request):
    return render(request,'payments/invoicenumber.html')







