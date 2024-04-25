package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.AdminService;

@WebServlet("/admindelete")
public class AdminDelete extends HttpServlet{
	AdminService adminService=new AdminService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String adno=req.getParameter("aid");
		int a=Integer.parseInt(adno);
		boolean res=adminService.deleteAdmin(a);
		
		if (res==true) {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("adminlogin.jsp");
			requestDispatcher.forward(req, resp);
		}else {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("admindelete.jsp");
			requestDispatcher.forward(req, resp);
		}
		
		
	}

}
