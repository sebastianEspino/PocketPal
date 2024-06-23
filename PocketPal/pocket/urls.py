from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login, name = "login"),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    
        
]



