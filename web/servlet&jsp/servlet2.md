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