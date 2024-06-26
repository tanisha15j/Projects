<%@page import="com.jsp.dto.Librarian"%>
<%@page import="java.util.List"%>
<%@page import="com.jsp.service.LibrarianService"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f2f2f2;
        text-align: center;
        margin: 20px auto;
    }

    h1 {
        color: #007BFF;
    }

    table {
        width: 80%;
        border-collapse: collapse;
        margin: 20px auto;
    }

    th, td {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: left;
    }

    th {
        background-color: #f2f2f2;
    }
</style>
</head>
<body>
<h1>List all Librarian</h1>
<%! LibrarianService librarianService=new LibrarianService();
List<Librarian> librarians=librarianService.getAllres();
%>
<table border="2px" cellspacing="0px" cellpadding="1px">
<tr>
<th>Id</th>
<th>Name</th>
<th>username</th>
<th>status</th>
<th>admin_Id</th>
</tr>

<% for(Librarian l:librarians) {%>
<tr>
<td><%= l.getId() %></td>
<td> <%= l.getName() %></td>
<td><%= l.getUsername() %></td>
<td><%= l.getStatus() %></td>
<td><%= (l.getAdmin()!=null)?l.getAdmin().getAdmin_id():" " %></td>
</tr>
<%} %>
</table>

</body>
</html>