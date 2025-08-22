# models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    def_str_(self):
        return self.name

# views.py
from django.shortcuts import render
from .models import Restaurant

def home_view(request):
    restaurant = Restaurant.objects.first() # get the first restaurant from DB
    restaurant_name = restaurant.name if restaurant else "MY Restaurant"
    return render(request,"home.html",{"restaurant_name": restaurant})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", view.home_view,name="home"),
 ]

 # templates/home.html
 "" "
 <!DOCTYPE html>
 <html>
 <head>
        <title>{{ request_name}}</title>
  </head>
  <body>
       <h1>Welcome to {{ restaurant_name }}</h1>
       <p>Enjoy delicious food at {{ restaurant_name }}!</p>
   </boby>
   </html>
   "" ""       

