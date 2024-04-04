from django.contrib import admin

from .models import Customer

class CustomersAdmin(admin.ModelAdmin):

    list_display = ['name', 'phone', 'address']

admin.site.register(Customer, CustomersAdmin)
