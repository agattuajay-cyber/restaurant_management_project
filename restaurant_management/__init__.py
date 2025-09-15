
from django.shortcuts import render

def menu_view(request):
    menu_items = [
        {"name": "Pizza", "price": 299},
        {"name": "Burger", "price": 149},
        {"name": "Pasta", "price": 199},
        {"name": "Salad", "price": 99},
    ]
    return render(request, "menu.html", {"menue_items": menu_items}) 


from django.urls import path
from .Views import menu_view

urlspatterns = [
    path("menu/", menu_view, name="menu"),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
]

<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="UTF-8">
     <title>Menu</title>
</head>
<body>
   <h1>Restaurent Menu</h1>
   <ul>
      {% for item in menu_items %}
         <1i>{{ item.name }} -{{ item.price}}</1i>
        {% endfor %} 
       </ul>
      </boby>
      </html>  

       




  