from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza, Toppings
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SpecialPizza, NewToppings
from django.shortcuts import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,"pizzas/index.html")
@login_required
def pizzas(request):
    """Show all topics"""
    pizzay= Pizza.objects.all()
    context={"pizza":pizzay}
    return render(request,"pizza.html",context)
def pizza(request,pizza_id):
    """show a single Pizza and all its toppings"""
    pizza=Pizza.objects.get(id=pizza_id)#gets one argument of id
    toppings=pizza.toppings_set.all() 
    context={'pizza':pizza,'topping':toppings}
    return render(request,'pizzas/pizzi.html',context)
def new_pizza(request):
    if request.method != "POST":
        form=SpecialPizza()
    else:
        form=SpecialPizza(request.POST)
        if form.is_valid():
            new_pizza=form.save(commit=False)
            new_pizza.fucking_owner=request.user
            new_pizza.save()
            return HttpResponseRedirect(reverse('pizzas:pizzas'))
    context={'form':form}
    return render(request,'pizzas/new_pizza.html',context)

def new_topping(request,pizza_id):

    """add a new Toppings for a Pizza"""
    pizzo=Pizza.objects.get(id=pizza_id)
    if pizzo.fucking_owner !=request.user:
        raise Http404
    if request.method != "POST":
        form = NewToppings()
    else:
        form = NewToppings(data=request.POST)
        if form.is_valid():
            newtopping=form.save(commit=False)
            newtopping.pizza=pizzo
            newtopping.save()
            return HttpResponseRedirect(reverse('pizzas:pizza',args=[pizza_id]))
    context={"pizzo":pizzo,"form":form}
    return render(request,"pizzas/newtopping.html",context)

def topping_edit(request,topping_id):
    """editing an existing topping"""
    topping=Toppings.objects.get(id=topping_id)
    pizzi=topping.pizza
    if pizzi.fucking_owner != request.user:
        raise Http404
    if request.method != "POST":
        #initial request;prefill form with current Topping
        form=NewToppings(instance=topping)
    else:
        form= NewToppings(instance=topping,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('pizzas:pizza',args=[pizzi.id]))

    context={'topping':topping,"pizza":pizzi,"form":form}
    return render(request,"pizzas/edit_topping.html",context)

    

