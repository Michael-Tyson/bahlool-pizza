from django import forms
from .models import Pizza, Toppings
class SpecialPizza(forms.ModelForm):
    class Meta:
        model= Pizza
        fields =['name']
        labels={"name":""}
class NewToppings(forms.ModelForm):
    class Meta:
        model= Toppings
        fields= ['name']
        labels={"name":""}
        widgets={"name":forms.Textarea(attrs={"rows":4,"cols":80})}

