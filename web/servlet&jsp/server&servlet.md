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

#### 컴파일 및 설정

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