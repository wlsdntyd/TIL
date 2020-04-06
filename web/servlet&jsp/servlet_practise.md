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

#### 여러 개의 Submit 버튼 사용하기 & 입력 데이터 배열로 받기

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Calc</title>
</head>
<body>
	<form action="add2" method="post">
		<label>num : </label><input type="text" name="num">
		<label>num : </label><input type="text" name="num">
		<label>num : </label><input type="text" name="num">
		<label>num : </label><input type="text" name="num">
		<input type="submit" name="btn" value="plus">
		<input type="submit" name="btn" value="div">
	</form>
</body>
</html>
```

```java
@WebServlet("/add2")
public class Add2 extends HttpServlet {
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setCharacterEncoding("UTF-8");
		response.setContentType("text/html ; UTF-8");
		PrintWriter out = response.getWriter();
		
		String[] nums = request.getParameterValues("num");
		String btn = request.getParameter("btn");
		int result = 0;
		
		if(btn.equals("plus")) {
			for(int i=0; i<nums.length; i++) {
				int num = Integer.parseInt(nums[i]);
				result += num;
			}
		}
		else if(btn.equals("div")) {
			for(int i=0; i<nums.length; i++) {
				int num = Integer.parseInt(nums[i]);
				if(i == 0)
					result += num;
				else
					result -= num;
			}
		}
		out.print("result : " + result);
	}
}
```

> getParameterValues 메소드 알아두자.