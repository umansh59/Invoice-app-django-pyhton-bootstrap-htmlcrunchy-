from django.contrib import admin
from .form import InvoiceForm

from .models import Invoice

admin.site.register(Invoice)

class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['name', 'invoice_number', 'invoice_date']
   form = InvoiceForm
   list_filter = ['name']
   search_fields = ['name', 'invoice_number']

# admin.site.register(Invoice, InvoiceAdmin)


