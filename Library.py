file=open("Navbar.html","w")
p="""
<html>
<head>
<title>Library</title>
<style>
.body{
box-sizing:border-box;
margin:0px;
padding:0px;
text-decoration:none;

}
.image{
background-image:url("library.jpg");
background-position:center;
background-size:cover;
position:relative;
width:100%;
height:100%
}
.header{
position:relative;
width:100%;
height:40px;
margin:0px
padding:0px
float:left;
}
.header .head-left{
width:33%;
height:40px;

float:left;
}
.header .head-left a{
display:block;
text-align:center;
color:white;
margin-top:25px;
padding:0px;
text-decoration:none;
}
.header .head-center{
width:33%;
height:40px;

float:left;
}
.header .head-right{
width:33%;
height:40px;

float:left;
}
.header .head-center a{
display:block;
text-align:center;
color:white;
margin-top:25px;
padding:0px;
text-decoration:none;
}
.header .head-right ul
{

list-style: none;
text-decoration:none;
}
.header .head-right ul li a {
float:left;
text-decoration:none;
background-color:black;
color:white;
margin:10px;

border-radius:10px;
}
.head-right ul li a:hover
{
color:lightblue;
}
/*Menu Bar*/
.menu-bar{
position:relative;


width:100%;
height:40px;

}
.menu-bar ul{
text-decoration:none;
list-style:none;


}
.menu-bar ul li a{
text-decoration:none;
float:left;
margin-top:10px;
margin-left:35px;
margin-right:35px;
border:1px solid grey;
background-color:#004a06;
font-size:1.2rem;
color:white;
border-radius:10px
}
.menu-bar ul li a:hover{
color:lightblue;
}
.icon{
width:60px;
height:50px;
float:left;
border-radius:25px;
}
.menu-bar ul input
{
margin-left:30%;
margin-right:5px;
margin-top:10px;
float:left;

}
#btn
{
margin-top:10px;
pointer:cursor;
border-radius:20px;
float:left;

}
/*Login Bar*/
.log{
position:relative;
width:100%;
text-align:center;
color:grey;
margin-top:10px;
padding-top:25px;
font-size:1.5rem;
height:20px;
}
.info{
position:relative;
width:100%;
text-align:center;
color:grey;
margin-top:10px;
padding-top:25px;
font-size:1.1rem;
height:200px;
}
/*Label*/
label {
font-size:2.0rem;
}
#Password1{

font-size:1.9rem;
margin-right:30px;
}
.info #name{
border-radius:20px;
margin-left:30px;
}
.info #branch{
border-radius:20px;
margin-left:25px;
}
.info #University{
border-radius:20px;
margin-left:4px;
}
.info #Password{
border-radius:20px;
margin-top:-5px;
margin-right:20px;
}
.footer{
margin-top:158px;
text-align:center;
color:grey;
</style>
</head>
<body >
<div class="image">
<div class="header">
<div class="head-left">
<a href="tel:+918509374208">+918509374208</a>
</div>
<div class="head-center">
<a href="">ihaque892@gmail.com</a>
</div>
<div class="head-right">
<ul>
<li><a href="https://www.google.com" >Google</a></li>
<li><a href="https://www.twitter.com">Twitter</a></li>
<li><a href="https://www.facebook.com">Facebook</a></li>
<li><a href="https://www.instagram.com">Instagram</a></li>
</ul>

</div>

</div>
<div class="menu-bar">
<ul>
<img class="icon" src="book.jpg">
<li><a href="#">Home</a></li>
<li><a href="#">Services</a></li>
<li><a href="#">Gallery</a></li>
<li><a href="#">About Us</a></li>
<input  type="text" placeholder="Explore">
<button id="btn" type="submit " value="submit" name="submit" >Submit</button>
</ul>

</div>
<div class="log">Login!</div>
<div class="info">
<div id="name">
<label for="name">Name:</label>
<textarea name="message" id="name" cols="30" rows="1" style="resize: none; "></textarea>
</div>
<div id="branch">
<label for="branch">Branch:</label>
<textarea name="message" id="branch" cols="30" rows="1" style="resize: none; "></textarea>
</div>
<div id="University">
<label for="University">University:</label>
<textarea name="message" id="University" cols="30" rows="1" style="resize: none; "></textarea>
</div>
<div id="Password">
<label for="Password" id="Password1">Password:</label>
<input type="password" id="Password" style:width:30px>
</div>
</div>
  <footer>
        <div class="footer" >
            Copyright &copy;www.MyLibrary.com.All Rights reserved.
        </div>
    </footer>
</div>
</div>
</body>

</html>
"""
file.write(p)
file.close()
