#### Session 객체에 상태 값 저장하기 (Application 과의 차이점)

> 이전 문서 server&servlet 의 맨 밑에 ServletContext를 설명했는데 이는 application 전역에서 사용할
>
> 수 있다는 것이고 session은 session 범주내에서만 사용할 수 있다는 것이다.
>
> 부연설명을 하자면 현재 접속한 사람의 공간이라고 볼 수 있다. 접속자 마다 공간이 달라진다.
>
> session을 저장소로 사용한다면 웹 브라우저 크롬과 엣지로 돌렸을 때 같은 공간이 아닌 것을 알 수 있다.
>
> 반면 크롬으로 두 개의 창을 띄워서 사용한다면 같은 공간임을 알 수 있다. 그건 하나의 프로세스를
>
> 여러 쓰레드로 제어하기 때문이다. 세션은 창을 끄면 공간이 사라진다.

## Session

클라이언트(사용자)가 웹 서버에 요청하여 처음 접속을 하면 JSP나 ASP 엔진이 사용자에게 유일한 ID를

부여하는데 이 ID를 세션이라 부른다. 클라이언트를 구분할 수 있는 유일한 수단으로 쓰인다.

그리고 세션은 사용자가 웹 브라우저를 열어 웹 서버에 접속한 뒤 브라우저를 종료하는 시점까지를 가리킨다.

밑 사진은 최초 접속 시 상태이고 다시 접속하게 되면 부여받은 ID로 서버상의 세션 스토리지에 접근할 수 있다.

즉 세션 스토리지의 데이터를 사용할 수 있다는 것! 아 더럽게 복잡하네

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\session&cookie.png)

#### Cookie ( 쿠키 )

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\session&cookie2.png)

> 쿠키는 클라이언트(사용자)의 저장소이다. 출력을 할 땐 addCookie(); , 쿠키를 읽을 땐 getCookie();

#### Servlet Context & Session & Cookie

> Servlet Context와 Application은 다르지만 일단 Application 이라하자.
>
> Application과 Session은 서버의 공간에 있는 것이고 Cookie는 클라이언트 공간에 있는 저장소이다.
>
> 이 세 개를 코드로 구현해보자.

```java
SevletContext application = request.getServletContext();
application.setAttribute("key", value);
application.getAttribute("key");

HttpSession session = request.getSession();
// session과 application 메소드 사용법은 비슷하다.

Cookie valueCookie = new Cookie("value", String.valueof(val));
Cookie opCookie = new Cookie("op", op);	// set 처럼 쓰인다고 보면 된다.

response.addCookie(valueCookie);	// client에게 전달이 됨. 저장됨.
response.addCookie(opCookie);

Cookie[] cookies = request.getCookies();	// cookie들을 읽음
int x = 0;
for(Cookie c : cookies)
	if(c.getName().equals("value")) {	// 해당 값을 찾는다.
		x = Integer.parseInt(c.getValue());
		break;
	}
String operator = "";
for(Cookie c : cookies)
	if(c.getName().equals("op")) {
		operator = c.getValue();
		break;
	}
```

> 쿠키는 세션과 다르게 메소드가 다소 복잡하다. 순서와 원리 정도는 잘 알아두자.

#### Cookie 를 이용한 계산기

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form action="add4" method="post">
		<label>num : </label><input type="text" name="num">
		<input type="submit" name="btn" value="+">
		<input type="submit" name="btn" value="-">
		<input type="submit" name="btn" value="=">
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

@WebServlet("/add4")
public class Add4 extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html ; UTF-8");
		PrintWriter out = response.getWriter();
		
		String num = request.getParameter("num");
		String btn = request.getParameter("btn");
		
		int number = 0;
		String b = "";
		if(btn.equals("=")) {
			Cookie[] cookies = request.getCookies();	// 쿠키 읽어드림
			
			for(Cookie c : cookies)
				if(c.getName().equals("num")) {
					number = Integer.parseInt(c.getValue());
					break;
				}
			
			for(Cookie c : cookies)
				if(c.getName().equals("btn")) {
					b = c.getValue();
					break;
				}
			int n = Integer.parseInt(num);
			
			if(b.equals("+"))
				out.print("result : " + (number + n));
			else
				out.print("result : " + (number - n));
		}
		else {
			Cookie n = new Cookie("num", num);	// 쿠키 생성
			Cookie bt = new Cookie("btn", btn);
            n.setPath("/add4");	// 해당 url에 대해 쿠키 값을 가져온다.
            n.setMaxAge(24*60*60); // 만료기간을 설정하는 메소드 브라우저가 꺼져도 살아있다.
			bt.setPath("/add4");
			response.addCookie(n);	// 클라이언트 저장소에 저장
			response.addCookie(bt);
		}
	}
}
```

> 후아 그동안 알고리즘 문제를 푼 덕일까 힘들었지만 만들었다. 5 + 를 입력했다면 5 = 을 입력하면 
>
> 5 + 5 = 10 해서 10이 출력이 된다.  단점이 여러 숫자를 연산할 수가 없다는 것이다.

#### Cookie 의 path 옵션

> 쿠키가 저장이 되고 가져오는 과정에서 경로를 설정하여 해당 url에 대해서만 쿠키 값을 가져올 수 있다.
>
> 위를 /add2 라고 설정한다면 /add4는 오류가 날 것이고 /add2 에서 확인해본다면 쿠키 값을 가져오는
>
> 것을 알 수 있다.

#### Cookie 의 만료 기간

> setMaxAge(); 메소드를 사용하지 않으면 브라우저가 닫힐 때 쿠키도 만료가 된다.
>
> 이 메소드를 설정해준다면 브라우저가 닫혀도 그 시간만큼은 만료가 되지 않고 저장소에 저장되어있다.
>
> 저장소는 메모리와 파일 두 곳에 모두 저장이 된다.