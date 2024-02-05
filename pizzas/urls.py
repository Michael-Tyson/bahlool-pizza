from django.urls import path
from . import views
app_name="pizzas"
urlpatterns=[
    path('homepage/',views.index,name='indexf'),
    path('pizzas/',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name="pizza"),
    path('new_pizza/',views.new_pizza,name="new_pizza"),
    path('new_toppings/<int:pizza_id>/',views.new_topping,name="new_topping"),
    path('topping_edit/<int:topping_id>/',views.topping_edit,name="edit_topping")
]
