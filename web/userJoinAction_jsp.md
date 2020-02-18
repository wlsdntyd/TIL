```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="user.UserDTO"%>	<!-- JSP에서  import하는 방식-->
<%@ page import="user.UserDAO"%>
<%@ page import="java.io.PrintWriter"%>
<%
	request.setCharacterEncoding("UTF-8");
	String userID = null;	// 참조할 때 많이 쓰는 방식.
	String userPassword = null;
	if(request.getParameter("userID") != null) {
		userID = (String) request.getParameter("userID");
	}
	if(request.getParameter("userPassword") != null) {
		userPassword = (String) request.getParameter("userPassword");
	}
	if(userID == null || userPassword == null) {	// 둘 중에 하나라도 비어있다면
		PrintWriter script = response.getWriter();	// 스크립트 구문 실행
		script.println("<script>");
		script.println("alert('입력이 안 된 사항이 있습니다.');");
		script.println("history.back();");	// 뒤로 가기 함수.
		script.println("</script>");
		script.close();
		return;
	}
	UserDAO userDAO = new UserDAO();
	int result = userDAO.join(userID, userPassword);
	if (result == 1) {
		PrintWriter script = response.getWriter();
		script.println("<script>");
		script.println("alert('회원가입에 성공했습니다.');");
		script.println("location.href = 'index.jsp';");
		script.println("</script>");
		script.close();
		return;
	}
%>
```

> 6번째 줄 request 부분 : 실제로 사용자가 보낸 데이터를 utf-8 이라는 즉 한글을 사용할 수 있는 형식으로 이렇게 데이터를 받아서 기본적으로 사용자에게 받아야 되는 정보를 다 정해준다.(userID와 userPasswrod)
>
> 그 다음 이제 리퀘스트 즉 사용자로부터 건너온 그 요청 패킷(회원가입)을 확인해서  userID란 이름의
>
> 변수가 존재하는지 확인한다. (!= null) 데이터가 존재한다면 각 userId, pw에 데이터를 저장해준다.