from django.contrib import admin

# Register your models here.
from .models import Customer, Order

admin.site.register(Customer)
admin.site.register(Order)