#### 동적인 계산기 만들기

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Calc</title>
<style>
	input { width: 50px; height: 50px; }
	.output { 
		height: 50px; background: #e9e9e9; font-size: 24px; 
		font-weight: bold; text-align: right; padding-right: 10px; }
</style>
</head>
<body>
	<form action="add5" method="post">
		<table>
			<tr>
				<td class="output" colspan="4">0</td>
			</tr>
			<tr>
				<td><input type="submit" name="operator" value="CE"></td>
				<td><input type="submit" name="operator" value="C"></td>
				<td><input type="submit" name="operator" value="BS"></td>
				<td><input type="submit" name="operator" value="/"></td>
			</tr>
			<tr>
				<td><input type="submit" name="value" value="7"></td>
				<td><input type="submit" name="value" value="8"></td>
				<td><input type="submit" name="value" value="9"></td>
				<td><input type="submit" name="operator" value="*"></td>
			</tr>
			<tr>
				<td><input type="submit" name="value" value="4"></td>
				<td><input type="submit" name="value" value="5"></td>
				<td><input type="submit" name="value" value="6"></td>
				<td><input type="submit" name="operator" value="-"></td>
			</tr>
			<tr>
				<td><input type="submit" name="value" value="1"></td>
				<td><input type="submit" name="value" value="2"></td>
				<td><input type="submit" name="value" value="3"></td>
				<td><input type="submit" name="operator" value="+"></td>
			</tr>
			<tr>
				<td><input type="submit" name="value" value="0"></td>
				<td><input type="submit" name="dot" value="."></td>
				<td><input type="submit" name="operator" value="="></td>
			</tr>
		</table>
	</form>
</body>
</html>
```

```java
package com.newlecture.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/calculation")
public class Calculation extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		Cookie[] cookies = request.getCookies();	// 쿠키 읽어드림
		String exp = "0";
		if(cookies != null) {
			System.out.println("12");
			for(Cookie c : cookies)
				if(c.getName().equals("exp")) {
					exp = c.getValue();
					break;
				}
		}
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		
		out.write("<!DOCTYPE html>");
		out.write("<html>");
		out.write("<head>");
		out.write("<meta charset=\"UTF-8\">");
		out.write("<title>Calc</title>");
		out.write("<style>");
		out.write("	input { width: 50px; height: 50px; }");
		out.write("	.output {");
		out.write("		height: 50px; background: #e9e9e9; font-size: 24px;"); 
		out.write("		font-weight: bold; text-align: right; padding-right: 10px; }");
		out.write("</style>");
		out.write("</head>");
		out.write("<body>");
		out.write("	<form action=\"add5\" method=\"post\">");
		out.write("		<table>");
		out.write("			<tr>");
		out.printf("				<td class=\"output\" colspan=\"4\">%s</td>", exp);
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"CE\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"C\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"BS\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"/\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"7\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"8\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"9\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"*\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"4\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"5\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"6\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"-\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"1\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"2\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"3\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"+\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"0\"></td>");
		out.write("				<td><input type=\"submit\" name=\"dot\" value=\".\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"=\"></td>");
		out.write("			</tr>");
		out.write("		</table>");
		out.write("	</form>");
		out.write("</body>");
		out.write("</html>");
	}
}
```

```java
package com.newlecture.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/add5")
public class Calculation2 extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		Cookie[] cookies = request.getCookies();	
		String value = request.getParameter("value");
		String operator = request.getParameter("operator");
		String dot = request.getParameter("dot");
		String exp = "";
		if(cookies != null) {
			System.out.println("12");
			for(Cookie c : cookies)
				if(c.getName().equals("exp")) {
					exp = c.getValue();
					break;
				}
		}
		if(operator != null && operator.equals("=")) {
			ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
			try {
				exp = String.valueOf(engine.eval(exp));
			} catch (ScriptException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else {
			exp += (value == null)?"":value;
			exp += (operator == null)?"":operator;
			exp += (dot == null)?"":dot;
		}
		Cookie expCookie = new Cookie("exp", exp);	
		response.addCookie(expCookie);
		response.sendRedirect("calculation");
	}
}
```

> 연속적인 계산이 가능해졌다. 

```java
package com.newlecture.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/onecalc")
public class OneCalc extends HttpServlet {
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Cookie[] cookies = request.getCookies();	// 쿠키 읽어드림
		String exp = "0";
		if(cookies != null)
			for(Cookie c : cookies)
				if(c.getName().equals("exp")) {
					exp = c.getValue();
					break;
				}
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		
		out.write("<!DOCTYPE html>");
		out.write("<html>");
		out.write("<head>");
		out.write("<meta charset=\"UTF-8\">");
		out.write("<title>Calc</title>");
		out.write("<style>");
		out.write("	input { width: 50px; height: 50px; }");
		out.write("	.output {");
		out.write("		height: 50px; background: #e9e9e9; font-size: 24px;"); 
		out.write("		font-weight: bold; text-align: right; padding-right: 10px; }");
		out.write("</style>");
		out.write("</head>");
		out.write("<body>");
		out.write("	<form method=\"post\">");
		out.write("		<table>");
		out.write("			<tr>");
		out.printf("				<td class=\"output\" colspan=\"4\">%s</td>", exp);
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"CE\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"C\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"BS\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"/\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"7\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"8\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"9\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"*\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"4\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"5\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"6\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"-\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"1\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"2\"></td>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"3\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"+\"></td>");
		out.write("			</tr>");
		out.write("			<tr>");
		out.write("				<td><input type=\"submit\" name=\"value\" value=\"0\"></td>");
		out.write("				<td><input type=\"submit\" name=\"dot\" value=\".\"></td>");
		out.write("				<td><input type=\"submit\" name=\"operator\" value=\"=\"></td>");
		out.write("			</tr>");
		out.write("		</table>");
		out.write("	</form>");
		out.write("</body>");
		out.write("</html>");	
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Cookie[] cookies = request.getCookies();	
		String value = request.getParameter("value");
		String operator = request.getParameter("operator");
		String dot = request.getParameter("dot");
		String exp = "";
		if(cookies != null)
			for(Cookie c : cookies)
				if(c.getName().equals("exp")) {
					exp = c.getValue();
					break;
				}
		if(operator != null && operator.equals("=")) {
			ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
			try {
				exp = String.valueOf(engine.eval(exp));
			} catch (ScriptException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if(operator != null && operator.equals("C")) {
			exp = "";
		}
		else {
			exp += (value == null)?"":value;
			exp += (operator == null)?"":operator;
			exp += (dot == null)?"":dot;
		}
		Cookie expCookie = new Cookie("exp", exp);
		if(operator != null && operator.equals("C"))
			expCookie.setMaxAge(0); // 만료 기한 0초로 만들어서 쿠키 삭제
		expCookie.setPath("/onecalc"); // 설정함으로서 다른 url에서 까지 쿠키 가져오는 것을 방지
		response.addCookie(expCookie);
		response.sendRedirect("onecalc");
	}
}
```

> 한 페이지에서의 모든 처리. 하나의 페이지이다 보니 action="" 이것을 지워도 된다.