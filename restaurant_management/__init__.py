# models.py
from django.db import models

class Restaurent(models.Models):
    name = models.CharField(max_length=100)

    def_str_(self):
        return self.name

# view.py from django.shortcuts import render
from .models import Restaurant 

def home_view(request):
    restaurant = Restaurant.objects.first() #get the first restaurant from DB
    restaurant_name = restaurant.name if restaurant else "My Restaurant"
    return render(request,"home.html",{"restaurent_name": restaurent_name})


#urls.py
from django.urls import path
from.import views

urlpatterns =[
    path("",view.home_view,name="home"),
]

#templates/home.html
"""
<DOCTYPE html>
<html>
<head>
    <title>{{ restaurent_name }}</title>
    <style>
      body {
        font-family: 'segoe UI',Arial,sans-serif;
        background: linear-gradient(to right,#f9f9f9, #e6e6e6);
        color:#333;
        margin: 0;
        padding: 20px 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2)
    }
    h1 {
        margin:0;
        font-size:2.5rem;
    }
    main {
        padding: 40px;
    }
    p {
        font-size: 1.2rem;
        color: #555;
    }
    footer {
        margin-top:50px;
        padding: 15px;
        background-color: #333;
        color: #eee;

    }
   </style>
  </head>
  <body>
      <header>
         <h1>Welcome to {{ restaurant_name }}</h1>
        <header>
        </main>
            <p>Enjoy delicious food at <strong>{{ restaurant_name }}</strong>!</p>
        </main>
        <footer>
            <p>&copy; {{ restaurant_name }} -All rights reserved.</p>
        </footer>
        </html>
        """                        