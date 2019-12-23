## Spring Boot 를 이용한 웹 응용개발

- sts 설치
  
  - java -jar lombok.jar
  
- lombok 설치
  
  - java -jar lombok.jar
  
- http 
  
  - post get put delete
  
- json
  
  - map중괄호 array list대괄호 object // @ResposeBody
  
- 컨트롤러 클래스 생성 
  
  - 메소드 @GetMapping / @RequestMapping
  
-  @ResponseBody @RestControlloer
  
  - json 또는 html
  
- @RequestParam , @ModelAttribute

- @GetMapping , @PostMapping

- ThymeLeaf

  ```html
  아이디:<span th:text="${user.userId}"></span><br>
  이름:<span th:text="${user.userName}"></span><br>
  나이:<span th:text="${user.userAge}"></span><br>
  ```

  > 타임리프 적용하는 방식.
  >
  > 노란 오류 없애는 경로 <html xmlns:th="http://www.thymeleaf.org">

  ```java
  @GetMapping("pagination")
  	 public String pagination(Model model, @RequestParam(defaultValue="1") int page) {
  	 int startPage = (page - 1) / 10 * 10 + 1;
  	 int endPage = startPage + 9;
  	 model.addAttribute("startPage", startPage);
  	 model.addAttribute("endPage", endPage);
  	 model.addAttribute("page", page);
  	 return "pagination";
  	 }
  ```

  > model : 컨트롤러에게 결과값을 전해주는 매개체 역할, 
  >
  > 사용하지 않을 시 파라미터에 변화가 없다(html화면에 변화가 없다).

  ```html
  <!DOCTYPE html>
  <html xmlns:th="http://www.thymeleaf.org">
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  	<th:block
  		th:each="pageNumber : ${#numbers.sequence(startPage, endPage)}">
  		<span th:if="${page} == ${pageNumber}" th:text="${pageNumber}"
  			style="font-weight: bold"></span>
  		<span th:unless="${page} == ${pageNumber}" th:text="${pageNumber}"></span>
  	</th:block>
  </body>
  </html>
  ```

  페이지 이동하는 html 형식. [1 2 3 4 5 6 7 8 9] [10 11 12 13 14 .... 19 20]

- shift + alt + A : 열 편집기능