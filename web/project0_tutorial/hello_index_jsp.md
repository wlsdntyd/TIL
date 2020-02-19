```jsp
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>드디어 되는건가?!?!</title>
</head>
<body>
	Hello World!!
	<form action="./userJoinAction.jsp" method="post">
		<input type="text" name="userID">
		<input type="password" name="userPassword">
		<input type="submit" value="회원가입">
	</form>
</body>
</html>
```

> "./userJoinAction.jsp" : 회원가입 요청 페이지라고 정의 해줌,
>
> userJoinAction.jsp 페이지로 post방식으로 데이터를 넘겨줌.