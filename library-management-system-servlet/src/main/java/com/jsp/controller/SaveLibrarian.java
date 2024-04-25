package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.dto.Librarian;
import com.jsp.service.LibrarianService;

@WebServlet("/libregistration")
public class SaveLibrarian extends HttpServlet {
	LibrarianService librarianService=new LibrarianService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String libname=req.getParameter("nameofuser");
		String email=req.getParameter("email");
		String pass=req.getParameter("password");
		
		Librarian librarian=new Librarian();
		librarian.setName(libname);
		librarian.setUsername(email);
		librarian.setPassword(pass);
		librarian.setStatus("authorized");
		
		librarianService.saveLibrarian(librarian);
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("librarianlogin.jsp");
		requestDispatcher.forward(req, resp);
		
	}

}

