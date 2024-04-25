package com.jsp.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.jsp.dto.Book;
import com.jsp.service.BookService;

@WebServlet("/addbook")
public class AddBook extends HttpServlet{
	BookService bookService=new BookService();
	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		String bname=req.getParameter("bookname");
		String aname=req.getParameter("authorname");
		Book book=new Book();
		book.setBook_name(bname);
		book.setAuthor(aname);
		book.setStatus("available");
		
		bookService.insertData(book);
		
		RequestDispatcher requestDispatcher=req.getRequestDispatcher("librarianportal.jsp");
		requestDispatcher.forward(req, resp);
	}

}

