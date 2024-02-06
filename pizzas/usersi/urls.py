from django.urls import path
from . import views
app_name="usersi"
urlpatterns=[
    path('login/',views.Login,name="login"),
    path('logout/',views.Logout,name="logout"),
    path('signup/',views.Signup,name="signup")
]
