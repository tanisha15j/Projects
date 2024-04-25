package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.LibrarianService;

@WebServlet("/liblogin")
public class LibrarianLogin extends HttpServlet{
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String libname=req.getParameter("email");
		String libpass=req.getParameter("password");
		
		LibrarianService librarianService=new LibrarianService();
		boolean res=librarianService.loginLibrarian(libname, libpass);
		
		if (res==true) {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("librarianportal.jsp");
			requestDispatcher.forward(req, resp);
		}else {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("librarianlogin.jsp");
			requestDispatcher.forward(req, resp);
		}
		
	}
	

}

