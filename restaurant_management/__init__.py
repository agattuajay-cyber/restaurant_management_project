<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,initial-scale=1.0">
   <title>Restaurant Homepage</title>
   <style>
   /*Rest */
   *{
    margin: 0;
    padding; 0;
    box-sizing: border_box;
    }

    body {
        font-family: Arial, sans-serif;
        backgound:#fafafa;
        color: #333;
        line-height: 1.6;
    }

    /* Navigation */
    nav {
        background: #2c3e50;
        padding:15px 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    nav.logo {
        color:#fff;
        font-size: 1.5rem;
        font-weight:bold;
    }

    nav ul {
        list-style: none:
        display: flex;
    }
    nav ul li {
        margin-left:20px;
    }
    nav ul li a {
        color: #fff;
        text-decoration: none;
        font-weight:bold;
        transition:color 0.3s;
    }

    /*Header */
    header {
        background: linear-gradient(rgba(0,0,0,0.5),rgba(0,0,0,0.5)),
                    url("https://via.placeholder.com/1600x600") center/cover no-repeat;
        color:white;
        text-align:center;
        padding:100px 20px;
    }
   header h1 {
    font-size:3rem;
    margin-bottom: 15px;
  }
   header p {
    font-size:1.2rem;
   }

   /*cards section */
   .container {
    max-wideth:1100px;
    margin:50px auto;
    display: grid;
    grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
    gap: 25px;
    padding:0 20px;
   }
   .card {
    background: white;
    border-radius:12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    overflow: hidden;
    transition: transform 0.3s ease;
   }
   .card:hover {
    transform:translateY(-5px);
   }

   .card img {
    width: 100%;
    height: 200px;
    object-fit: cover;
   }

   .card h3 {
    margin:15px;
    font-size: 1.2rem;
   }

   .card p {
    margin: 0 15px 15px;
    color: #555;
   }
   .btn {
    display: inline-block;
    margin: 0 15px 15px;
    padding: 10px 15px;
    background: #f39c12;
    color: white;
    text-decoration: none;
    border-radius: 6px;
    font-weight: bold;
    transition:background 0.3s;
   }
   .btn:hover {
    background: #e67e22;
   }

   /* Footer */
    footer {
        background: #2c3e50;
        color:white;
        text-align: center;
        padding: 20px;
        margin-top: 40px;
       }
      </style>
     </head>
    <body>

     <!---Navigation--->
     <nav>
       <div class="logo">My Restaurant</div>
       <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Menu</a></li>
          <li><a href="#">Contact</a></li>
         </ul>
        </nav>

        <!--- Hero Header---->
        <header>
          <h1>Welcome to My Restaurant</h1>
          <p>Delicious food,cozy atmosphere friendly service</p>
        </header>

       <!--cards section --->
       <div class="container">
          <div class="card">
            <img src="https://via.placeholder.com/400*250" alt="Dish">
            <h3>Special Dish 1</h3>
            <p>A short description of this dish goes here.</p>
            <a href="#" class="btn">Order Now</a>
          </div>
          <div class="card">
            <img src="https"//via.placeholder.com/400*250" alt="Dish">
            <h3>Special Dish 2</h3>
            <p>A short description of this dish goes here.</p>
            <a href="#" class="btn">Order Now</a>
          </div>
          <div class="card">
           <img src="http://via.placeholder.com/400*250" alt="Dish">
           <h3>Special Dish 3</h3>
           <p>A short description of this dish goes here.</p>
           <a href="#" class="btn">Order Now</a>
         </div>
        </div>

        <!---footer---->
        <footer>
           2025 My Restaurant.ALL Rights Reserved.
         </footer>

      </body>
      </html>     