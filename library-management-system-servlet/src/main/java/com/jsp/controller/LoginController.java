package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.AdminService;

@WebServlet("/login")
public class LoginController extends HttpServlet {
	AdminService adminService = new AdminService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String username = req.getParameter("email");
		String password = req.getParameter("password");
		
		boolean res=adminService.loginAdmin(username, password);
		if (res==true) {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("Adminportal.jsp");
			requestDispatcher.forward(req, resp);
		}else {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("adminlogin.jsp");
			requestDispatcher.include(req, resp);
		}
		
	}
}