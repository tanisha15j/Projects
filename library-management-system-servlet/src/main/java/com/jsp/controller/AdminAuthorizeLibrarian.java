package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.AdminService;

@WebServlet("/authorizelibrarian")
public class AdminAuthorizeLibrarian extends HttpServlet{
	AdminService adminService=new AdminService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String libid=req.getParameter("libid");
		String aid=req.getParameter("adminid");
		
		int librarianid=Integer.parseInt(libid);
		int adminid=Integer.parseInt(aid);
		
		boolean res=adminService.approveLibrarian(librarianid, adminid);
		
		if (res==false) {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("adminauthorizelib.jsp");
			requestDispatcher.forward(req, resp);
		}else {
			RequestDispatcher requestDispatcher=req.getRequestDispatcher("Adminportal.jsp");
			requestDispatcher.forward(req, resp);
		}
	}

}