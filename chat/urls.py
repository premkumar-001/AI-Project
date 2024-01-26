from django.urls import path
from . import views

urlpatterns =[

     path('register',views.register,name="register"),
     path('sign_in',views.sign_in,name="sign_in"),
     path('home',views.home,name="home"),
     path('chat',views.chat,name="chat"),
     path('log_out',views.log_out,name="log_out")
     
     
]