# SpringBoot

- Client >>> Server [(request) 요청할 시]

  - 주로 Get , Post 방식 put, delete도 포함
  - @RequestParam : ? 뒤에 파라미터 지정, 컨트롤러 메소드의 인자명과 동일
  - @ModelAttribute : 모델 클래스의 변수명 동일

- Server >>> Client [(response)응답,반응이 옴]

  - 크게 html, json, image, download

  > 주로 웹서버, 다양한 서버가 존재한다.

```java
public class HtmlController {
@GetMapping("html/string")
public String html() {
return "html/string";
}
```

> 위에 있는 html/string 형식을 제일 많이 쓴다

th:each 반복문 숙지

```html
th:each="pageNumber : ${#numbers.sequence(startPage, endPage)}
```

> th : thymeleaf 의 형식 sequence : start부터 end까지 숫자를 가져옴
>
> th:each 반복문 sequence에서 따온 번호들을 pagenumber에 대입

```html
<th:block th:each="page : ${#numbers.sequence(start,end)}">
	<span th:if = "${now_page == page}" th:text = "${page}"></span>
	<a href="#" th:unless="${now_page == page}">[[${page}]]</a>
</th:block>
```

> th:if 조건이 참이면 th : if

```html
@RequestParam int now_page = @RequestParam(defaultValue = "1") int now_page
```

- HTTP : Hyper Text Transfer Protocol [Secure] 
  - Stateless 상태를 기억하지 못함 정보를 기억하고 있는 쿠키?
- client(cookie)         <>          server(session공간
- AOP(관점지향 프로그래밍)(임시저장공간) : 1순위 제일 강력함
  - 어떠한 클래스든, 어떠한 메소드든 대상, 스프링의 기능
- Filter : 접속하는 주소(url)를 대상
  - 자바의 고유 기능
- Interceptor : 접속하는 주소(url)를 대상
  - 스프링의 기능

- Ioc /DI (inversion of Control / Dependency Injection) : 별로 안중요

  - 만드는 IoC 

- framework 

- advice pointcut aspect

  ```
  
  ```

  