from django import forms
from .models import *


#форма для заказа
class Order(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        exclude = ['user','datetime','all_price']