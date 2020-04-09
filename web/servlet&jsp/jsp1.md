#### JSP 내장 객체(servlet 코드)

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\jsp-builtin.png)

> jsp 파일의 servlet 코드를 살펴보면 위의 네모 박스 총 8개의 내장 객체가 있는 것을 알 수 있다.
>
> 각 객체가 가지고 있는 메소드들은 인터넷을 보며 익혀두자.

#### JSP Spaghetti and MVC model1

> jsp 페이지에서 스파게티라 함은 코드 블럭들이 여러 군데 난잡하게 있는 경우이다.
>
> 이를 보완하기 위해 MVC model1이 나왔다. 모델1은 입력 블록, 출력 블록으로 나누어서 두 군데로
>
> 나누어서 코드를 보다 간결화 한것이다.

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\model1.png)

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
int num = 0; 
String num_ = request.getParameter("n");
if(num_ != null && !num_.equals(""))
	num = Integer.parseInt(num_);
String result;
if(num % 2 != 0)
	result = "홀수";
else
	result = "짝수";
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<%=result %> 입니다.
</body>
</html>
```

#### MVC model2 : 컨트롤러(Servlet)와 뷰(JSP)가 물리적으로 분리된 형태

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\model2-2.png)

```java
package com.newlecture.web;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/spag")
public class Spag extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int num = 0; 
		String num_ = request.getParameter("n");
		if(num_ != null && !num_.equals(""))
			num = Integer.parseInt(num_);
		String result;
		if(num % 2 != 0)
			result = "홀수";
		else
			result = "짝수";
		request.setAttribute("result", result);
		// redirect 새로운 요청할 때 쓰임
		// forward : 일을 이어갈 때 쓰임		dispatcher : 급파하다
		RequestDispatcher dispatcher = request.getRequestDispatcher("spag.jsp");
		dispatcher.forward(request, response); 
		// 해당 페이지로 현재까지 작업한 내용(req,res)을 이어지게 해줌(연결 다리 느낌?)
		// 실행할 땐 무조건 controller 에서 할 것 데이터가 컨트롤러에 있으니
	}
}
```

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>	// forward 메소드를 통해 데이터를 이어줘서 get으로 값을 얻어낸다.
	<%=request.getAttribute("result") %> 입니다.
</body>
</html>
```

> dispatcher의 forward 메소드로 데이터를 jsp파일과 이어줄 수 있다는 것을 알아두자.