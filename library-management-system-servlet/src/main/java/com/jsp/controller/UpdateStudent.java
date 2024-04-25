package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.service.StudentService;

@WebServlet("/updatestudent")
public class UpdateStudent extends HttpServlet {
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		int sid=Integer.parseInt(req.getParameter("studentid"));
		int sidyear=Integer.parseInt(req.getParameter("year"));
		StudentService studentService=new StudentService();
		studentService.updateData(sid, sidyear);
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("librarianportal.jsp");
		requestDispatcher.forward(req, resp);
	}

}
