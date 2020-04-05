#### Form 태그를 이용한 post방식의 요청 & 응답

```html
<body>
	<form action="add" method="post">
		<lable>X : <input type="text" name="x"></lable>
		<lable>Y : <input type="text" name="y"></lable>
		<input type=submit value="더하기">
	</form>
</body>
```

```java
@WebServlet("/add")
public class calAdd extends HttpServlet {
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response)
			throws ServerException, IOException {
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html; charset=UTF-8");
		PrintWriter out = response.getWriter();
		String x_ = request.getParameter("x");
		String y_ = request.getParameter("y");		
		int x = 0;
		int y = 0;		
		if(!x_.equals("") && x_ != null)
			x = Integer.parseInt(x_);
		if(!y_.equals("") && y_ != null)
			y = Integer.parseInt(y_);		
		out.printf("덧셈의 결과 : %d", (x + y));
	}
}
```

> 듣는 건 쉬웠으나 혼자하려니 힘들다.