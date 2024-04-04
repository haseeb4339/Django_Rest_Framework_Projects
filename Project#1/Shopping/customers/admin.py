from django.contrib import admin

from .models import Customers

class CustomersAdmin(admin.ModelAdmin):

    list_display = ['name', 'phone', 'address']

admin.site.register(Customers, CustomersAdmin)
