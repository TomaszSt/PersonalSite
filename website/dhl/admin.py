from django.contrib import admin
from .forms import BrokerUserForm, OrderForm
from .models import BrokerUser, Order


class BrokerUserRegister(admin.ModelAdmin):
    list_display = ["__unicode__", "email", "name"]
    form = BrokerUserForm

class OrderList(admin.ModelAdmin):
    list_display = ["__unicode__", 'orderId','senderId','premiumUser','packageImage','user','status']
    form = OrderForm


admin.site.register(BrokerUser, BrokerUserRegister)
admin.site.register(Order,OrderList)
