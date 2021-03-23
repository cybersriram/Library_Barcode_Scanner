from django.urls import path
from . import views
urlpatterns =[
    path("",views.index,name="index"),path("get",views.index,name="index"),path("convert",views.con,name="convert"),path("register",views.register,name="register")
]