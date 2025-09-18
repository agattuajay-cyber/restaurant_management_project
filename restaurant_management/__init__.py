# settings.py (add at bottom)
RESTAURANT_NAME = "tasty Bites"
RESTAURENT_PHONE = "+91-9876543210"

# views.py
from django.conf import settingsfrom django.shortcuts import render

def homepage(request):
    context = {
        "restaurent_name": settings.RESTAURENT_NAME,
        "restaurent_phone":settings.RESTAURENT_PHONE,
    }
    return render(request,"homepage.html",context) 

    #urls.py
    from django.urls import path
    from. import views

    urlpatterns = [
        path('',views.homepage,name='homepage'),
    ]

    <!---templates/homepage.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{{ restaurent_name }}</title>
    </head>
    <body style="font-family:Arial,sans-serif; background-color:#f9f9f9; margin:0; padding:0;">

    <!---Header--->
    <div style="background-color:#4CAF50; PADDING:20PX; text-align:center; color:white;">
       <h1 style="margin:0;">Welcome to {{ restaurent_name }}</h1>
    </div>

    <!---Content --->
    <div style="padding:20px; text-align:center;">
        <p style="font-size:18px;"> Contact us at:<strong>{{ restaurent_phone }}</strong></p>
    <div>

</body>
</html>           





























       




  