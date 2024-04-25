package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.AdminService;

@WebServlet("/updateadmin")
public class UpdateAdmin extends HttpServlet {
	AdminService adminService=new AdminService();
	
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		String adminnewpassword = req.getParameter("adminnewpass");
		int id=Integer.parseInt(req.getParameter("adminid"));
		adminService.updateadminpass(id, adminnewpassword);
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("Adminportal.jsp");
			requestDispatcher.forward(req, resp);
		
	}
}

