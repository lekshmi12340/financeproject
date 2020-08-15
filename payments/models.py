from django.db import models

from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
class invoice(models.Model):

    invoicenumber = models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    clientname = models.CharField(max_length=50)
    clientemailid = models.EmailField()
    projectname = models.CharField(max_length=50)
    amounttobecharged=models.IntegerField()

    class Meta:
        verbose_name_plural= "client details"
    def __str__(self):
        return self.invoicenumber

class dbupdate(models.Model):
    yourinvoice=models.CharField(max_length=50, blank=True, null=True, validators=[alphanumeric])
    class Meta:
        verbose_name_plural= "invoicedetails"
    def __str__(self):
        return self.yourinvoice




# Create your models here.
