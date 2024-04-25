package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.StudentService;

@WebServlet("/returnbook")
public class ReturnBook extends HttpServlet{
	StudentService studentService=new StudentService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int bkid=Integer.parseInt(req.getParameter("bookid"));
		
		studentService.returnBookById(bkid);
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("studentportal.jsp");
		requestDispatcher.forward(req, resp);
		
	}

}

