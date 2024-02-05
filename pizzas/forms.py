from django import forms
from .models import Pizza, Toppings
class SpecialPizza(forms.ModelForm):
    class Meta():
        model=Pizza
        fields=["name"]
        label={"name":""}
class NewToppings(forms.ModelForm):
    class Meta():
        model= Toppings
        fields=["name"]
        label={"name":""}