package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.dto.Student;
import com.jsp.service.StudentService;

@WebServlet("/addstudent")
public class StudentSave extends HttpServlet{
	StudentService studentService=new StudentService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String studentname=req.getParameter("stname");
		String studentdegree=req.getParameter("stdeg");
		String studentstream=req.getParameter("ststream");
		int studentyear=Integer.parseInt(req.getParameter("styear"));
		String sname = req.getParameter("uname");
		String password = req.getParameter("pass");
 		
		Student student =new Student();
		student.setName(studentname);
		student.setDegree(studentdegree);
		student.setStream(studentstream);
		student.setYear(studentyear);
		student.setUsername(sname);
		student.setPassword(password);
		studentService.insertData(student);
		
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("studentlogin.jsp");
		requestDispatcher.forward(req, resp);
		
	}

}
