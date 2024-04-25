package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.dto.Admin;
import com.jsp.service.AdminService;

@WebServlet("/adminregister")
public class AdminRegister extends HttpServlet{
	AdminService adminService=new AdminService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String name=req.getParameter("nameofadmin");
		String admin_email=req.getParameter("email");
		String admin_pass=req.getParameter("password");
		
		Admin admin=new Admin();
		admin.setAdmin_name(name);
		admin.setAdmin_email(admin_email);
		admin.setAdmin_pass(admin_pass);
		adminService.saveAdmin(admin);
		
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("adminlogin.jsp");
		requestDispatcher.forward(req, resp);
		
	}

}