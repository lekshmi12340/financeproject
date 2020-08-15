from django.contrib import admin

from payments.models import invoice, dbupdate

admin.site.register(invoice)
admin.site.register(dbupdate)
# Register your models here.
