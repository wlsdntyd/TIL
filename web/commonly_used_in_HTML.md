## HTML 에서 자주 쓰이는 것들

- <%@ page import="java.io.PrintWriter"%>

> JSP에서 자바 스크립트를 출력하고자 할 때 많이 사용하는 방식, 스크립트 구문을 쉽게
>
> 클라이언트에게 출력해줄 수 있다.

- [Html] rel 속성 (relationship, 관계)

> rel 속성은 링크된 문서와의 관계를 지정한다. 브라우저나 검색엔진에게 링크 관계에 대한 정보를 주어
>
> 사용자의 요청에 더 정확한 대응이 가능하게 해준다.
>
> 따라서 이 rel은 주로 href 속성이 있을 때 지정하고 주로 헤더에서 사용해왔다.

- section(부분) 태그 : html5 부터 적용가능.

> html문서의 독립적인 구획을 나타내며, 더 적합한 의미를 가진 요소가 없을 때 사용한다.
>
> div보다 강조하는 느낌을 주고 싶을 때 사용하는 것 같다.

- **modal** 의 속성들.

> modal을 띄우는데 필수적인 속성은 button 태그의 경우 data-target 과 data-toggle 속성이 있다.
>
> data-target의 value는 버튼 클릭 시 모달로 띄우고자하는 id값을 # 붙여서 연결해주는 것이다.
>
> data-toggle의 value는 모달기능을 실행하는 속성이다. button 태그의 data-dismiss 속성을 적용하면
>
> 모달을 닫는 기능이 적용된다.

- span 태그 : 아이콘 역할을 한다. 닫기 버튼 아이콘 같은?

```jsp
<section class="container">	<!-- html5 부터 적용되는 section태그 -->
			<a class="btn btn-primary mx-1 mt-2" data-toggle="modal" href="#registerModal">등록하기</a>
			<a class="btn btn-danger mx-1 mt-2" data-toggle="modal" href="#reportModal">신고</a>
	</section>
	<div class="modal fade" id="registerModal" tabindex="-1" role="dialog" aria-labelledby="modal" aria-hidden="true">
		<div class="modal-dialong">
			<div class="modal-content">
				<div class="modal-header">
					<h5 class="modal-title" id="modal">평가 등록</h5>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">			<span aria-hidden="true">&times;</span>		
					</button>
				</div>
				<div class="modal-body">				
				</div>
			</div>
		</div>
	</div>
```

- NBSP (no-break space) : &nbsp

> 공백 문자를 연속으로 여러 개 삽입하고 싶을 경우 &nbsp를 쓰면 정상적으로 출력된다.

- div class="form-row" & div class="form-group col-sm-6"

> **bootstrap이 가장 많이 사용되는 이유이자 반응형 웹페이지를 만들기 위해 가장 많이 사용이 필요한 기능.**
>
> **bootstrap의 가장 핵심적인 기능으로 작동원리와 어떻게 활용할 수 있을지 고민한다면 유용할거다.**
>
> row : 가로로 그룹 지을 칼럼들의 집합이다. 칼럼은 총 12칼럼이 있는 것으로 정의하여 배치할 %에 따라
>
> 클래스를 결정하면 된다. 예를 들어 col-xs-4 를 세 번 쓴다거나 등등 12칼럼이 넘어가면 새로운
>
> 줄로 칼럼이 배치된다. 12칼럼보다 적다면 오른쪽에 공백이 생긴다.

- div class="container" & "container-fluid"

> container : bootstrap에서 반응형으로 사용할 html요소들을 둘러 싸는 기본 클래스로 제공된다.
>
> container-fluid 클래스를 사용하면 화면에 꽉 차면서 크기에 따라 다르게 반응할 수 있는 wrapper를 
>
> 사용하게 되는 것이다. 