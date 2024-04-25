<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<style>
        *{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            /* font-family: 'Poppin'; */
        }

        body{
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: rgb(6, 6, 44);
        }

        .container{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }

        .container a{
            position: relative;
            width: 300px;
            height: 65px;
            display: inline-block;
            background-color: #fff;
            margin: 20px;
            font-family: 'Young Serif', serif;
            
        }
        .container a::before,
        .container a::after{
            content: '';
            position: absolute;
            inset: 0;
            background-color: aqua;
            transition: 0.5s;
        }
        /* span{
            text-align: center;
            padding-top: 5%;
        } */

        .container input:nth-child(1){
            text-align: center;
            padding-top: 5%;
        }
        
        

         .container a:before, 
         .container a:after{ 
             background: linear-gradient(45deg,#00ccff,#0e150e,#0e150e,#d400d4); 
         } 
         
         
/*         .container .get:nth-child(1):before, */
/*         .container .get:nth-child(1):after{ */
/*             background: linear-gradient(45deg,#a21e6b,#0e150e,#0e150e,#0be33a); */
/*         } */
/*         .container a:nth-child(3):before, */
/*         .container a:nth-child(3):after{ */
/*             background: linear-gradient(45deg,#d400d4,#0e150e,#0e150e,#00ccff); */
/*         } */

        .container a:hover:before{
            inset: -3px;
        }
        .container a:hover::after{
            inset: -3px;
        }
        .container a input{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: inline-block;
            background-color: rgb(6, 6, 44);
            display: flex;
            z-index: 10;
            justify-content: center;
            align-self: center;
            font-size: 1.2em;
            text-transform: uppercase;
            letter-spacing: 2px;
            color: #fff;
            border: 1px solid #0c2061;
            cursor: pointer;
        }
        .container a input::before{
            content: '';
            position: absolute;
            top: 0;
            left: -50%;
            width: 100%;
            height: 100%;
            
        }

        .heading h3{
            color: #fff;
            /* font-family: 'Libre Baskerville', serif; */
            font-family: 'Spline Sans Mono', monospace;
            
            /* font-family: 'Young Serif', serif; */
            margin-right: 200px;
            font-size: 35px;
            word-spacing: 10px;
        }
        .heading  p{
            color: #fff;
            margin-right: 200px;
            font-size: 15px;
            word-spacing: 10px;
            text-align: center;
        }

    </style>
<body>
<div class="heading">
        <h3>Admin Portal</h3><br>
        
    </div>
	<div class="container">
    <form action="adminportal"method="post" class="login-form">
        <a><input type="submit" value="librarian Detail" name="getlibrarian" class="login-btn"></a> <br> <br>
        <a><input type="submit" value="delete account" name="delete" class="login-btn"></a> <br> <br>
        <a><input type="submit" value="Update Password" name="update" class="login-btn"></a> <br> <br>
        <a><input type="submit" value="Authorized Librarian" name="authorize" class="login-btn"></a> <br> <br>
        
    </form>
    </div>

</body>
</html>