#### 서버 기본 구성

1] 실행 환경

1. 웹 서버 - 클라이언트에게 요청을 받고, 코드 실행한 결과를 (WAS에게 받아) 요청자에게 전달하는 주체(실체) 
2. WAS(web application server) - 코드를 실행하고, 실행된 결과를 보여주는 서비스 환경(Tomcat같은)

2] 실행 대상

1. Server App - WAS에서 실행되는 것으로, "동적인 방식으로" 문서를 만들기 위한 코드   
2. Servlet  - Serv + -let을 합친 말로 Server Application let(작은 조각, 파편)의 줄임말로 추측,
3. 내용은 Server App 각각의 코드를 의미(index.html 같은 것들)

#### 간단한 출력 Servlet 코드

```java
import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;

public class Nana extends HttpServlet {
	public void service(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		OutputStream os = response.getOutputStream(); // 출력 객체 get
		PrintStream out = new PrintStream(os, true); // 밑에서 설명
		out.println("Hello Servlet!!");
	}
}
// PrintWriter out = response.getWriter();
// out.println("Hello Servlet!!");
```

> 저 세 줄을 안 쓰고 주석 처리해놓은 두 줄로도 처리가 가능하다. IO(입출력)에는 Stream과 Writer가 있다.
>
> print객체에 대해 설명하자면 글자 buffer를 일정 양을 채우면 출력을 하는데(false) 채워지기 전에 출력을
>
> 할 경우 true로 설정하면 된다. 그리고 **문자를 쓰는데 다국어라면 Writer계열을 쓰는게 맞다.**

#### 메모장에서의 컴파일 및 설정

> 메모장으로 작성을 했다면(저장할 시 .java로) 명령 프롬프트로 javac 파일명.java를 적으면 된다.
>
> 근데 servlet api는 외부 api이기때문에 톰캣 폴더에서 가져와야한다.(lib/servlet-api)
>
> 중간 과정은 인터넷을 참고하자. 클래스 파일을 얻었다면 webapps/ROOT/WEB-INF 로 와서 classes란
>
> 폴더를 만들고 안에 넣자. WEB-INF는 다른 폴더와 다르게 클라이언트에서 접근할 수 있는 것이 아니다.
>
> 넣었다면 web.xml 을 메모장으로 열어 맨 밑 display태그 바로 위에 밑 Servlet코드를 적자.
>
> 톰캣 서버를 활성화 시킨 후 /hello 로 들어가면 출력이 제대로 이루어진 것을 볼 수 있을 것이다.

#### Servlet 추가 코드

```
 <servlet>
<servlet-name>na</servlet-name>
<servlet-class>Nana</servlet-class>
 </servlet>

 <servlet-mapping>
<servlet-name>na</servlet-name>
<url-pattern>/hello</url-pattern>
 </servlet-mapping>
```

> **제일 중요한 것은 들여쓰기다.** 톰캣 서버가 활성화되지 않는 경우는 servlet 추가 시 name이 중복되거나
>
> 스펠링이 틀렸거나 하는 경우가 대부분이다. 오류 원인 못 찾아서 시간 날린 거 생각하면 ,,,,,,,,
>
> 쨋든 위 코드를 잘 봐두자.

#### eclipse 에서의 servlet

> 개발 환경은 jee를 쓰면 되고, WAS 인 톰캣은 servlet코드를 실행하고 화면에 뿌려주는 역할을 하고
>
> eclipse에서는 그 servlet코드(html 등등)를 수정,삭제한다고 볼 수 있다. servlet을 추가할 시 
>
> WebContent > WEB-INF 하위 폴더에 톰캣 폴더 안의 web.xml파일을 복사해서 추가해줘야한다.
>
> 소스코드 수정 시 소스파일이 패키지 안에 존재할 시 web.xml에서 다음과 같이 수정해야한다.
>
> <servlet-class>com.newlecture.web.Nana</servlet-class> 폴더.폴더.파일 식으로,,,

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\servlet설정.png)

> 위 사진처럼 경로 설정을 / 로 지정해줄 시 localhost/JSPPrj/hello 에서 JSPPrj를 생략할 수 있게 해준다.
>
> localhost/hello 로 바로 가능하다.

#### Annotation 을 이용한 URL 매핑

```java
@WebServlet("/hi")	// 어노테이션. /hi 로 이동하면 밑 실행 코드를 뿌려준다.
public class Nana extends HttpServlet {
	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		PrintWriter out = resp.getWriter();
		out.println("Hello~~jinoo");
	}
}
// metadata-complete="false">
```

> 여기서 주의할 점은 **web.xml 파일에서 위 주석 처리한 코드를 true에서 false로 바꿔주어야한다.**
>
> true일 시 web.xml에서만 metadata를 찾는 것이고 false를 해야 다른 곳의 metadata까지 찾는다.

#### 크롬과 엣지 웹 브라우저에서의 코드 해석

```java
@WebServlet("/hi")
public class Nana extends HttpServlet {
	@Override
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		PrintWriter out = resp.getWriter();
		
		for(int i=0; i<100; i++)
			out.println((i+1) + "Hello Servlet!!<br />");
	}
}
// Chrome : 1Hello Servlet!!<br />
// Edge : 1Hello Servlet!!
```

> 위 코드를 크롬과 엣지에서 실행해보면 크롬에서는 br태그까지 출력이 되는 반면 Edge에서는 안 보인다.
>
> 이유는 Edge에선 html로 해석하는 반면 크롬에선 text로 해석하기 때문인데 브라우저에 컨텐츠 형식을
>
> 알려주지 않아서 그렇다. 그렇기에 자의적으로 해석하여 뿌려준 것이다. 이를 보완하기 위해 출력 형식을
>
> 지정해주어야 한다.

#### 한글이 깨지는 이유

> 위 코드에 한글을 적어서 출력을 해본다면 ?로 나오는 것을 볼 수 있다. 톰캣의 기본 인코딩 방식이
>
> 문자 하나에 1바이트를 차지하기 때문인데 영어는 1바이트로 출력이 가능한 반면 한글은 최소 2바이트를
>
> 차지하기 때문이다. 이럴 때는 utf-8로 인코딩을 하고 타입을 html과 utf-8로 지정해주어야한다.
>
> 지정해준다면 위의 br 태그는 정상적으로 실행될 것이다.

```java
response.setCharacterEncoding("UTF-8");
response.setContentType("text/html; charset=UTF-8");	// html로 타입을 지정.
```

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\content-type.png)

#### GET 요청과 쿼리 스트링

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\get.png)

```java
response.setCharacterEncoding("UTF-8");
response.setContentType("text/html; charset=UTF-8");
PrintWriter out = response.getWriter();

int cnt = Integer.parseInt(request.getParameter("cnt"));

for(int i=0; i<cnt; i++)
	out.println((i+1) + "안녕 Servlet!!<br />");
```

> 바깥 코드는 위와 같다.

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\getquery.png)

> ?cnt=3 과 ?cnt= , ?, 아무것도 없는것 총 네 가지 경우의 수를 고려해서 코드를 짜야한다. "" 이것은 null값이
>
> 아닌 그냥 빈공간으로써 처리를 해주어야한다.

```java
response.setCharacterEncoding("UTF-8");
response.setContentType("text/html; charset=UTF-8");
PrintWriter out = response.getWriter();

String cnt_ = request.getParameter("cnt");
int cnt = 100;

if(cnt_ != null && !cnt_.equals(""))	// 총 4가지 중 3가지 경우의 수 고려한 코드
	cnt = Integer.parseInt(cnt_);		// 부족하긴하다. 문자열이 들어갈 수도 있으니

for(int i=0; i<cnt; i++)
	out.println((i+1) + "안녕 Servlet!!<br />");
```

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	환영합니다.<br >
	<a href="hi">인사하기</a><br>	// /hi 페이지로 이동
	<a href="hi?cnt=3">3번 인사하기</a><br>	// /hi?cnt=3 페이지로 이동
</body>
</html>
```

> 그냥 하면 재미없으니 WebContent 밑에 index.html을 만들어 구현해보자.

#### Form 태그를 이용한 GET 요청(사용자 입력을 통한 요청)

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\getform.png)

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<div>
		<form action="hi">
			<div>
				<label>"안녕하세요"를 몇번 출력할까요? </label>
			</div>
			<div>
				<input type="text" name="cnt" />
				<input type="submit" value="출력" />
			</div>
		</form>
	</div>
</body>
</html>
```

> hello.html을 작성해서 실행해보자.

#### UTF-8 초기 값으로 설정하기

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\utf_setting.png)

#### 입력 내용이 많을 경우 POST 요청으로 처리해야 한다.

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<div>
		<form action="notice-reg" method="post">
			<div>
				<label>제목 : </label><input name="title" type="text" >
			</div>
			<div>
				<label>내용 : </label>
				<textarea name="content"></textarea>
			</div>
			<div>
				<input type="submit" value="등록" />
			</div>
		</form>
	</div>
</body>
</html>
```

```java
package com.newlecture.web;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/notice-reg")	// notice-reg 라는 url-pattern으로 이동
public class noticeReg extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
        request.setCharacterEncoding("UTF-8");	// 설정 안 해주면 요청 보낼 때 한글깨짐.
		PrintWriter out = response.getWriter();
		
		String title = request.getParameter("title");
		String content = request.getParameter("content");
		
		out.print(title + "<br>");
		out.print(content);
	}
}
```

> 내용이 많을 경우 또는 회원가입 같은 경우는 POST 방식이 적합하다. 응답할 때 UTF-8로 지정해주어서
>
> 한글이 잘 출력됐다면 **요청(request)을 할 때도 한글로 서버에 요청을 보낸다면 서버로 보내는 과정에**
>
> **한글이 깨지지 않도록 요청 인코딩 형식 또한 UTF-8로 지정해주어야 한다.**

#### 번거로운 인코딩을 위한 Filter 인터페이스 기능

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\filter.png)

> 여기서 WAS는 톰캣에 해당한다 볼 수 있고 인코딩 형식이야 그냥 톰캣의 server.xml 파일에서 형식을
>
> UTF-8로 바꾸면 되긴 하지만 다른 서블릿들에게도 영향을 주게 되므로 원하는 서블릿들에게만
>
> 인코딩 형식을 지정해줄 수 있는 것을 Filter 기능이라 한다. 

```xml
<filter>
    <filter-name>characterEncodingFilter</filter-name>
    <filter-class>com.newlecture.web.filter.CharacterEncodingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>characterEncodingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

> web.xml 에서의 filter 기능 추가 /* 는 모든 url에 적용되도록. 적는게 귀찮다면 annotation으로도 가능하다.

```java
package com.newlecture.web.filter;

import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;

@WebFilter("/*")	// annotation을 이용한 필터 방법.
public class CharacterEncodingFilter implements Filter {

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		
		request.setCharacterEncoding("UTF-8");	// 번거로움을 줄여준다.
		//System.out.println("before filter");
		chain.doFilter(request, response);	// chain은 servlet으로 req와 res를 넘겨준다.
		//System.out.println("after filter");
	}
}
```

> 매번 서블릿에 인코딩 형식을 지정해주는 번거로움을 없애주는 Filter 인터페이스의 기능이다.

#### ServletContext 저장소 객체 사용

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\servletcontext.png)

> 서블릿에서 요청이 들어올 시 메모리에 올라왔다가 바로 사라지는데 서블릿 Context를 이용하면 저장을
>
> 해둘 수 있다. 서블릿 Context는 서블릿들이 자원을 공유할 수 있는 저장소라고 볼 수 있다.
>
> Application 에서는 application 저장소라고 한다.

```java
@WebServlet("/add3")
public class serialAdd extends HttpServlet {

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html ; UTF-8");
		ServletContext application = request.getServletContext();
		PrintWriter out = response.getWriter();
		
		String num = request.getParameter("val");
		String op = request.getParameter("operator");
		int n = Integer.parseInt(num);
		if(op.equals("+"))
			application.setAttribute("ns", n);
		else if(op.equals("-"))
			application.setAttribute("ns", -n);
		else {
			int result = (Integer)application.getAttribute("ns");
			out.print("result : " + result);
		}
	}
}
// HttpSession session = request.getSession(); 세션 객체도 사용할 수 있다.
```

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Serial Calc</title>
</head>
<body>
	<form action="add3" method="post">
		<label>value : </label><input type="text" name="val">
		<input type="submit" value="+" name="operator">
		<input type="submit" value="-" name="operator">
		<input type="submit" value="=" name="operator">		
	</form>
</body>
</html>
```

> 대충 해봤는데 값을 하나씩 밖에 못한다. 다 계산해서 출력하는 건 나중에 꼭 해봐야지

