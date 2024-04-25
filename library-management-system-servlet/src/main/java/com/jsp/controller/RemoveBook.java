package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.BookService;

@WebServlet("/removebook")
public class RemoveBook extends HttpServlet {
	BookService bookService=new BookService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int id=Integer.parseInt(req.getParameter("libid"));
		bookService.deleteData(id);
		
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("librarianportal.jsp");
		requestDispatcher.forward(req, resp);
		
	}

}
