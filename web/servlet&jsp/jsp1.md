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

#### Expression Language

```java
String[] names = {"jinoo", "ji", "no"};
request.setAttribute("names", names);
Map<String, Object> notice = new HashMap<String, Object>();
notice.put("id", 1);
notice.put("title", "EL은 좋다?");
request.setAttribute("notice", notice);
pageContext.setAttribute("result",100);
// ----------------------------------------- 위 : Servlet, 밑 : JSP
<%=request.getAttribute("result") %> 입니다.<br >
${result}<br>	// 우선순위로 인해 위의 페이지 저장소에서 값 가져오게됨.
${names[0]}<br>
${notice.id}<br>
${pageScope.result}<br>	// 해당 영역에서 찾을 때 쓰임.(scope)
${param.n} // 파라미터 값 출력
${header.accept}	// 헤더의 accept값 출력
${empty param.n}	// 비어있는지(""), null 인지 체크, 비어있다면 true
${empty param.n ? '값이 비어있습니다':param.n}	// 체크해서 값이 있다면 값을 출력.
```

> EL : get메소드를 통해 데이터를 불러오는 번거로움을 줄여주는 언어라 볼 수 있다.
>
> 상황에 따른 사용법을 익혀두자. EL에는 연산자 또한 있으니 lt, gt, le, ge, empty 등 알아두자

#### Page, Request, Session, Application 4 가지의 저장소

각 저장소에 키 이름이 같을 경우 위 적은 순수대로 우선 순위로 인해 값을 가져온다.

해당 영역에서 값을 가져올 경우 requestScope.키이름 이런 식으로 접근하면 된다.

#### 4가지의 코드 블록

```
<% %>
<%= %>
<%! %>
<%@ %>
```

#### html 에서 JSP로 바꿀 시 주의 사항

한글이 깨지는 경우 ALT + Enter로 속성에 들어간 뒤 인코딩을 UTF-8로 바꿔주면 된다.

또한 jsp페이지에서 페이지 인코딩을 해줘야한다.

```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
```

#### MVC (model view controller)

화면을 뿌려주는 view,  데이터를 제어하는 controller, 둘 사이를 잇는 데이터(모델) model 이라해서

MVC 라 한다.