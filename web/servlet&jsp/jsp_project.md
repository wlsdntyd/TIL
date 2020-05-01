#### JSP를 이용한 프로젝트

JSP에서 JDBC를 이용하기 위해 사전에 jdbc.jar 파일을 맞는 위치시켜야 한다.

WebContent > WEB-INF > lib > 위치

> list 페이지

```jsp
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
String sql = "SELECT * FROM NOTICE";

Class.forName("oracle.jdbc.driver.OracleDriver");
Connection con = DriverManager.getConnection(url, "newlec", "1234");
Statement st = con.createStatement();
ResultSet rs = st.executeQuery(sql);
%>
<!DOCTYPE html>
<html>

<head>
    <title>코딩 전문가를 만들기 위한 온라인 강의 시스템</title>
    <meta charset="UTF-8">
    <title>공지사항목록</title>
    
    <link href="/css/customer/layout.css" type="text/css" rel="stylesheet" />
    <style>
    
        #visual .content-container{	
            height:inherit;
            display:flex; 
            align-items: center;
            
            background: url("../../images/customer/visual.png") no-repeat center;
        }
    </style>
</head>

<body>
    <!-- header 부분 -->

    <header id="header">
        
        <div class="content-container">
            <!-- ---------------------------<header>--------------------------------------- -->

            <h1 id="logo">
                <a href="/index.html">
                    <img src="/images/logo.png" alt="뉴렉처 온라인" />

                </a>
            </h1>

            <section>
                <h1 class="hidden">헤더</h1>

                <nav id="main-menu">
                    <h1>메인메뉴</h1>
                    <ul>
                        <li><a href="/guide">학습가이드</a></li>

                        <li><a href="/course">강좌선택</a></li>
                        <li><a href="/answeris/index">AnswerIs</a></li>
                    </ul>
                </nav>

                <div class="sub-menu">

                    <section id="search-form">
                        <h1>강좌검색 폼</h1>
                        <form action="/course">
                            <fieldset>
                                <legend>과정검색필드</legend>
                                <label>과정검색</label>
                                <input type="text" name="q" value="" />
                                <input type="submit" value="검색" />
                            </fieldset>
                        </form>
                    </section>

                    <nav id="acount-menu">
                        <h1 class="hidden">회원메뉴</h1>
                        <ul>
                            <li><a href="/index.html">HOME</a></li>
                            <li><a href="/member/login.html">로그인</a></li>
                            <li><a href="/member/agree.html">회원가입</a></li>
                        </ul>
                    </nav>

                    <nav id="member-menu" class="linear-layout">
                        <h1 class="hidden">고객메뉴</h1>
                        <ul class="linear-layout">
                            <li><a href="/member/home"><img src="/images/txt-mypage.png" alt="마이페이지" /></a></li>
                            <li><a href="/notice/list.html"><img src="/images/txt-customer.png" alt="고객센터" /></a></li>
                        </ul>
                    </nav>

                </div>
            </section>

        </div>
        
    </header>

	<!-- --------------------------- <visual> --------------------------------------- -->
	<!-- visual 부분 -->
	
	<div id="visual">
		<div class="content-container"></div>
	</div>
	<!-- --------------------------- <body> --------------------------------------- -->
	<div id="body">
		<div class="content-container clearfix">

			<!-- --------------------------- aside --------------------------------------- -->
			<!-- aside 부분 -->


			<aside class="aside">
				<h1>고객센터</h1>

				<nav class="menu text-menu first margin-top">
					<h1>고객센터메뉴</h1>
					<ul>
						<li><a class="current"  href="/customer/notice">공지사항</a></li>
						<li><a class=""  href="/customer/faq">자주하는 질문</a></li>
						<li><a class="" href="/customer/question">수강문의</a></li>
						<li><a class="" href="/customer/event">이벤트</a></li>
						
					</ul>
				</nav>


	<nav class="menu">
		<h1>협력업체</h1>
		<ul>
			<li><a target="_blank" href="http://www.notepubs.com"><img src="/images/notepubs.png" alt="노트펍스" /></a></li>
			<li><a target="_blank" href="http://www.namoolab.com"><img src="/images/namoolab.png" alt="나무랩연구소" /></a></li>
						
		</ul>
	</nav>
					
			</aside>
			<!-- --------------------------- main --------------------------------------- -->



		<main class="main">
			<h2 class="main title">공지사항</h2>
			
			<div class="breadcrumb">
				<h3 class="hidden">경로</h3>
				<ul>
					<li>home</li>
					<li>고객센터</li>
					<li>공지사항</li>
				</ul>
			</div>
			
			<div class="search-form margin-top first align-right">
				<h3 class="hidden">공지사항 검색폼</h3>
				<form class="table-form">
					<fieldset>
						<legend class="hidden">공지사항 검색 필드</legend>
						<label class="hidden">검색분류</label>
						<select name="f">
							<option  value="title">제목</option>
							<option  value="writerId">작성자</option>
						</select> 
						<label class="hidden">검색어</label>
						<input type="text" name="q" value=""/>
						<input class="btn btn-search" type="submit" value="검색" />
					</fieldset>
				</form>
			</div>
			
			<div class="notice margin-top">
				<h3 class="hidden">공지사항 목록</h3>
				<table class="table">
					<thead>
						<tr>
							<th class="w60">번호</th>
							<th class="expand">제목</th>
							<th class="w100">작성자</th>
							<th class="w100">작성일</th>
							<th class="w60">조회수</th>
						</tr>
					</thead>
					<tbody>
					<%while(rs.next()){ %>		
					<tr>
						<td><%=rs.getInt("ID") %></td>
						<td class="title indent text-align-left"><a href="detail.jsp?id=<%=rs.getInt("ID")%>"><%=rs.getString("TITLE") %></a></td>
						<td><%=rs.getString("WRITER_ID") %></td>
						<td>
							<%=rs.getDate("REGDATE") %>	
						</td>
						<td><%=rs.getInt("HIT") %></td>
					</tr>
					<%} %>		
					
					
					
					</tbody>
				</table>
			</div>
			
			<div class="indexer margin-top align-right">
				<h3 class="hidden">현재 페이지</h3>
				<div><span class="text-orange text-strong">1</span> / 1 pages</div>
			</div>

			<div class="margin-top align-center pager">	
		
	<div>
		
		
		<span class="btn btn-prev" onclick="alert('이전 페이지가 없습니다.');">이전</span>
		
	</div>
	<ul class="-list- center">
		<li><a class="-text- orange bold" href="?p=1&t=&q=" >1</a></li>
				
	</ul>
	<div>
		
		
			<span class="btn btn-next" onclick="alert('다음 페이지가 없습니다.');">다음</span>
		
	</div>
	
			</div>
		</main>
		
			
		</div>
	</div>

    <!-- ------------------- <footer> --------------------------------------- -->
        <footer id="footer">
            <div class="content-container">
                <h2 id="footer-logo"><img src="/images/logo-footer.png" alt="회사정보"></h2>
    
                <div id="company-info">
                    <dl>
                        <dt>주소:</dt>
                        <dd>서울특별시 </dd>
                        <dt>관리자메일:</dt>
                        <dd>admin@newlecture.com</dd>
                    </dl>
                    <dl>
                        <dt>사업자 등록번호:</dt>
                        <dd>111-11-11111</dd>
                        <dt>통신 판매업:</dt>
                        <dd>신고제 1111 호</dd>
                    </dl>
                    <dl>
                        <dt>상호:</dt>
                        <dd>뉴렉처</dd>
                        <dt>대표:</dt>
                        <dd>홍길동</dd>
                        <dt>전화번호:</dt>
                        <dd>111-1111-1111</dd>
                    </dl>
                    <div id="copyright" class="margin-top">Copyright ⓒ newlecture.com 2012-2014 All Right Reserved.
                        Contact admin@newlecture.com for more information</div>
                </div>
            </div>
        </footer>
    </body>
    
    </html>
	<%
	rs.close();
	st.close();
	con.close();
	%>
```

> detail.jsp 페이지

```jsp
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
int id = Integer.parseInt(request.getParameter("id"));
String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
String sql = "SELECT * FROM NOTICE WHERE ID=?";

Class.forName("oracle.jdbc.driver.OracleDriver");
Connection con = DriverManager.getConnection(url, "newlec", "1234");
PreparedStatement st = con.prepareStatement(sql);
st.setInt(1, id);
ResultSet rs = st.executeQuery();
rs.next();
%>
<!DOCTYPE html>
<html>

<head>
    <title>코딩 전문가를 만들기 위한 온라인 강의 시스템</title>
    <meta charset="UTF-8">
    <title>공지사항목록</title>
    
    <link href="/css/customer/layout.css" type="text/css" rel="stylesheet" />
    <style>
    
        #visual .content-container{	
            height:inherit;
            display:flex; 
            align-items: center;
            
            background: url("../../images/customer/visual.png") no-repeat center;
        }
    </style>
</head>

<body>
    <!-- header 부분 -->

	<header id="header">
        
        <div class="content-container">
            <!-- ---------------------------<header>--------------------------------------- -->

            <h1 id="logo">
                <a href="/index.html">
                    <img src="/images/logo.png" alt="뉴렉처 온라인" />

                </a>
            </h1>

            <section>
                <h1 class="hidden">헤더</h1>

                <nav id="main-menu">
                    <h1>메인메뉴</h1>
                    <ul>
                        <li><a href="/guide">학습가이드</a></li>

                        <li><a href="/course">강좌선택</a></li>
                        <li><a href="/answeris/index">AnswerIs</a></li>
                    </ul>
                </nav>

                <div class="sub-menu">

                    <section id="search-form">
                        <h1>강좌검색 폼</h1>
                        <form action="/course">
                            <fieldset>
                                <legend>과정검색필드</legend>
                                <label>과정검색</label>
                                <input type="text" name="q" value="" />
                                <input type="submit" value="검색" />
                            </fieldset>
                        </form>
                    </section>

                    <nav id="acount-menu">
                        <h1 class="hidden">회원메뉴</h1>
                        <ul>
                            <li><a href="/index.html">HOME</a></li>
                            <li><a href="/member/login.html">로그인</a></li>
                            <li><a href="/member/agree.html">회원가입</a></li>
                        </ul>
                    </nav>

                    <nav id="member-menu" class="linear-layout">
                        <h1 class="hidden">고객메뉴</h1>
                        <ul class="linear-layout">
                            <li><a href="/member/home"><img src="/images/txt-mypage.png" alt="마이페이지" /></a></li>
                            <li><a href="/notice/list.html"><img src="/images/txt-customer.png" alt="고객센터" /></a></li>
                        </ul>
                    </nav>

                </div>
            </section>

        </div>
        
    </header>

	<!-- --------------------------- <visual> --------------------------------------- -->
	<!-- visual 부분 -->
	
	<div id="visual">
		<div class="content-container"></div>
	</div>
	<!-- --------------------------- <body> --------------------------------------- -->
	<div id="body">
		<div class="content-container clearfix">

			<!-- --------------------------- aside --------------------------------------- -->
			<!-- aside 부분 -->


			<aside class="aside">
				<h1>고객센터</h1>

				<nav class="menu text-menu first margin-top">
					<h1>고객센터메뉴</h1>
					<ul>
						<li><a class="current"  href="/customer/notice">공지사항</a></li>
						<li><a class=""  href="/customer/faq">자주하는 질문</a></li>
						<li><a class="" href="/customer/question">수강문의</a></li>
						<li><a class="" href="/customer/event">이벤트</a></li>
						
					</ul>
				</nav>


	<nav class="menu">
		<h1>협력업체</h1>
		<ul>
			<li><a target="_blank" href="http://www.notepubs.com"><img src="/images/notepubs.png" alt="노트펍스" /></a></li>
			<li><a target="_blank" href="http://www.namoolab.com"><img src="/images/namoolab.png" alt="나무랩연구소" /></a></li>
						
		</ul>
	</nav>
					
			</aside>
			<!-- --------------------------- main --------------------------------------- -->

			<main>
				<h2 class="main title">공지사항</h2>
				
				<div class="breadcrumb">
					<h3 class="hidden">breadlet</h3>
					<ul>
						<li>home</li>
						<li>고객센터</li>
						<li>공지사항</li>
					</ul>
				</div>
				
				<div class="margin-top first">
						<h3 class="hidden">공지사항 내용</h3>
						<table class="table">
							<tbody>
								<tr>
									<th>제목</th>
									<td class="text-align-left text-indent text-strong text-orange" colspan="3"><%=rs.getString("TITLE") %></td>
								</tr>
								<tr>
									<th>작성일</th>
									<td class="text-align-left text-indent" colspan="3"><%=rs.getDate("REGDATE") %>	</td>
								</tr>
								<tr>
									<th>작성자</th>
									<td><%=rs.getString("WRITER_ID") %></td>
									<th>조회수</th>
									<td><%=rs.getString("HIT") %></td>
								</tr>
								<tr>
									<th>첨부파일</th>
									<td colspan="3"><%=rs.getString("FILES") %></td>
								</tr>
								<tr class="content">
									<td colspan="4"><%=rs.getString("CONTENT") %></td>
								</tr>
							</tbody>
						</table>
					</div>
					
					<div class="margin-top text-align-center">
						<a class="btn btn-list" href="list.jsp">목록</a>
					</div>
					
					<div class="margin-top">
						<table class="table border-top-default">
							<tbody>
								
								<tr>
									<th>다음글</th>
									<td colspan="3"  class="text-align-left text-indent">다음글이 없습니다.</td>
								</tr>
								
								<tr>
									<th>이전글</th>
									<td colspan="3"  class="text-align-left text-indent"><a class="text-blue text-strong" href="">스프링 DI 예제 코드</a></td>
								</tr>
								
							</tbody>
						</table>
					</div>							
			</main>					
		</div>
	</div>

    <!-- ------------------- <footer> --------------------------------------- -->

        <footer id="footer">
            <div class="content-container">
                <h2 id="footer-logo"><img src="/images/logo-footer.png" alt="회사정보"></h2>
    
                <div id="company-info">
                    <dl>
                        <dt>주소:</dt>
                        <dd>서울특별시 </dd>
                        <dt>관리자메일:</dt>
                        <dd>admin@newlecture.com</dd>
                    </dl>
                    <dl>
                        <dt>사업자 등록번호:</dt>
                        <dd>111-11-11111</dd>
                        <dt>통신 판매업:</dt>
                        <dd>신고제 1111 호</dd>
                    </dl>
                    <dl>
                        <dt>상호:</dt>
                        <dd>뉴렉처</dd>
                        <dt>대표:</dt>
                        <dd>홍길동</dd>
                        <dt>전화번호:</dt>
                        <dd>111-1111-1111</dd>
                    </dl>
                    <div id="copyright" class="margin-top">Copyright ⓒ newlecture.com 2012-2014 All Right Reserved.
                        Contact admin@newlecture.com for more information</div>
                </div>
            </div>
        </footer>
    </body>
    
    </html>
    <%
	rs.close();
	st.close();
	con.close();
	%>
```

#### MVC(model view controller) model1 방식으로 변경

> list.jsp 는 똑같다. 코드 블록을 다 위로 올려서 controller와 view 파트로 나누었다.

```jsp
<%@page import="java.util.Date"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
int id = Integer.parseInt(request.getParameter("id"));
String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
String sql = "SELECT * FROM NOTICE WHERE ID=?";
Class.forName("oracle.jdbc.driver.OracleDriver");
Connection con = DriverManager.getConnection(url, "newlec", "1234");
PreparedStatement st = con.prepareStatement(sql);
st.setInt(1, id);
ResultSet rs = st.executeQuery();
rs.next();

String title = rs.getString("TITLE");
Date regdate = rs.getDate("REGDATE");
String writerId = rs.getString("WRITER_ID");
String hit = rs.getString("HIT");
String files = rs.getString("FILES");
String content = rs.getString("CONTENT");
   
rs.close();
st.close();
con.close();
%>
<!DOCTYPE html>
<html>

<head>
    <title>코딩 전문가를 만들기 위한 온라인 강의 시스템</title>
    <meta charset="UTF-8">
    <title>공지사항목록</title>
    
    <link href="/css/customer/layout.css" type="text/css" rel="stylesheet" />
    <style>
    
        #visual .content-container{	
            height:inherit;
            display:flex; 
            align-items: center;
            
            background: url("../../images/customer/visual.png") no-repeat center;
        }
    </style>
</head>

<body>
    <!-- header 부분 -->

	<header id="header">
        
        <div class="content-container">
            <!-- ---------------------------<header>--------------------------------------- -->

            <h1 id="logo">
                <a href="/index.html">
                    <img src="/images/logo.png" alt="뉴렉처 온라인" />

                </a>
            </h1>

            <section>
                <h1 class="hidden">헤더</h1>

                <nav id="main-menu">
                    <h1>메인메뉴</h1>
                    <ul>
                        <li><a href="/guide">학습가이드</a></li>

                        <li><a href="/course">강좌선택</a></li>
                        <li><a href="/answeris/index">AnswerIs</a></li>
                    </ul>
                </nav>

                <div class="sub-menu">

                    <section id="search-form">
                        <h1>강좌검색 폼</h1>
                        <form action="/course">
                            <fieldset>
                                <legend>과정검색필드</legend>
                                <label>과정검색</label>
                                <input type="text" name="q" value="" />
                                <input type="submit" value="검색" />
                            </fieldset>
                        </form>
                    </section>

                    <nav id="acount-menu">
                        <h1 class="hidden">회원메뉴</h1>
                        <ul>
                            <li><a href="/index.html">HOME</a></li>
                            <li><a href="/member/login.html">로그인</a></li>
                            <li><a href="/member/agree.html">회원가입</a></li>
                        </ul>
                    </nav>

                    <nav id="member-menu" class="linear-layout">
                        <h1 class="hidden">고객메뉴</h1>
                        <ul class="linear-layout">
                            <li><a href="/member/home"><img src="/images/txt-mypage.png" alt="마이페이지" /></a></li>
                            <li><a href="/notice/list.html"><img src="/images/txt-customer.png" alt="고객센터" /></a></li>
                        </ul>
                    </nav>

                </div>
            </section>

        </div>
        
    </header>

	<!-- --------------------------- <visual> --------------------------------------- -->
	<!-- visual 부분 -->
	
	<div id="visual">
		<div class="content-container"></div>
	</div>
	<!-- --------------------------- <body> --------------------------------------- -->
	<div id="body">
		<div class="content-container clearfix">

			<!-- --------------------------- aside --------------------------------------- -->
			<!-- aside 부분 -->


			<aside class="aside">
				<h1>고객센터</h1>

				<nav class="menu text-menu first margin-top">
					<h1>고객센터메뉴</h1>
					<ul>
						<li><a class="current"  href="/customer/notice">공지사항</a></li>
						<li><a class=""  href="/customer/faq">자주하는 질문</a></li>
						<li><a class="" href="/customer/question">수강문의</a></li>
						<li><a class="" href="/customer/event">이벤트</a></li>
						
					</ul>
				</nav>


	<nav class="menu">
		<h1>협력업체</h1>
		<ul>
			<li><a target="_blank" href="http://www.notepubs.com"><img src="/images/notepubs.png" alt="노트펍스" /></a></li>
			<li><a target="_blank" href="http://www.namoolab.com"><img src="/images/namoolab.png" alt="나무랩연구소" /></a></li>
						
		</ul>
	</nav>
					
			</aside>
			<!-- --------------------------- main --------------------------------------- -->

			<main>
				<h2 class="main title">공지사항</h2>
				
				<div class="breadcrumb">
					<h3 class="hidden">breadlet</h3>
					<ul>
						<li>home</li>
						<li>고객센터</li>
						<li>공지사항</li>
					</ul>
				</div>
				
				<div class="margin-top first">
						<h3 class="hidden">공지사항 내용</h3>
						<table class="table">
							<tbody>
								<tr>
									<th>제목</th>
									<td class="text-align-left text-indent text-strong text-orange" colspan="3"><%=title %></td>
								</tr>
								<tr>
									<th>작성일</th>
									<td class="text-align-left text-indent" colspan="3"><%=regdate %></td>
								</tr>
								<tr>
									<th>작성자</th>
									<td><%=writerId %></td>
									<th>조회수</th>
									<td><%=hit %></td>
								</tr>
								<tr>
									<th>첨부파일</th>
									<td colspan="3"><%=files %></td>
								</tr>
								<tr class="content">
									<td colspan="4"><%=content %></td>
								</tr>
							</tbody>
						</table>
					</div>
					
					<div class="margin-top text-align-center">
						<a class="btn btn-list" href="list.jsp">목록</a>
					</div>
					
					<div class="margin-top">
						<table class="table border-top-default">
							<tbody>
								
								<tr>
									<th>다음글</th>
									<td colspan="3"  class="text-align-left text-indent">다음글이 없습니다.</td>
								</tr>
								
								<tr>
									<th>이전글</th>
									<td colspan="3"  class="text-align-left text-indent"><a class="text-blue text-strong" href="">스프링 DI 예제 코드</a></td>
								</tr>
								
							</tbody>
						</table>
					</div>							
			</main>					
		</div>
	</div>

    <!-- ------------------- <footer> --------------------------------------- -->

        <footer id="footer">
            <div class="content-container">
                <h2 id="footer-logo"><img src="/images/logo-footer.png" alt="회사정보"></h2>
    
                <div id="company-info">
                    <dl>
                        <dt>주소:</dt>
                        <dd>서울특별시 </dd>
                        <dt>관리자메일:</dt>
                        <dd>admin@newlecture.com</dd>
                    </dl>
                    <dl>
                        <dt>사업자 등록번호:</dt>
                        <dd>111-11-11111</dd>
                        <dt>통신 판매업:</dt>
                        <dd>신고제 1111 호</dd>
                    </dl>
                    <dl>
                        <dt>상호:</dt>
                        <dd>뉴렉처</dd>
                        <dt>대표:</dt>
                        <dd>홍길동</dd>
                        <dt>전화번호:</dt>
                        <dd>111-1111-1111</dd>
                    </dl>
                    <div id="copyright" class="margin-top">Copyright ⓒ newlecture.com 2012-2014 All Right Reserved.
                        Contact admin@newlecture.com for more information</div>
                </div>
            </div>
        </footer>
    </body>    
    </html>
```

#### MVC model2 로 변경

model2 같은 경우 컨트롤러와 뷰가 물리적으로 분리되어있기 때문에 컨트롤러(Servlet)를 추가하였다.

request 저장소를 이용하여 데이터를 뷰(JSP)로 넘겨주는 방식으로 구현하였다.(forward)

뷰 같은 경우 필요한 데이터를 쓸 때 request.getAttribute() 메소드를 사용하면 되므로 뷰는 생략.

```java
package com.newlecture.web.controller;

import java.io.IOException;
import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/notice/detail")
public class NoticeDetailController extends HttpServlet{
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		int id = Integer.parseInt(request.getParameter("id"));
		String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
		String sql = "SELECT * FROM NOTICE WHERE ID=?";
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con = DriverManager.getConnection(url, "newlec", "1234");
			PreparedStatement st = con.prepareStatement(sql);
			st.setInt(1, id);
			ResultSet rs = st.executeQuery();
			rs.next();

			String title = rs.getString("TITLE");
			Date regdate = rs.getDate("REGDATE");
			String writerId = rs.getString("WRITER_ID");
			String hit = rs.getString("HIT");
			String files = rs.getString("FILES");
			String content = rs.getString("CONTENT");
			
			request.setAttribute("title", title);
			request.setAttribute("regdate", regdate);
			request.setAttribute("writerId", writerId);
			request.setAttribute("hit", hit);
			request.setAttribute("files", files);
			request.setAttribute("content", content);
			   
			rs.close();
			st.close();
			con.close();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		// forward
		request.getRequestDispatcher("/notice/detail.jsp").forward(request, response);
	}
}
```

#### Entity 를 이용한 Model 데이터 구조화하기

```java
package com.newlecture.web.entity;

import java.sql.Date;

public class Notice {
	private int id;
	private String title;
	private Date regdate;
	private String writerId;
	private String hit;
	private String files;
	private String content;
	
	public Notice(int id, String title, Date regdate, String writerId, String hit, String files, String content) {
		this.id = id;
		this.title = title;
		this.regdate = regdate;
		this.writerId = writerId;
		this.hit = hit;
		this.files = files;
		this.content = content;
	}
	
	public Notice() {
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public Date getRegdate() {
		return regdate;
	}

	public void setRegdate(Date regdate) {
		this.regdate = regdate;
	}

	public String getWriterId() {
		return writerId;
	}

	public void setWriterId(String writerId) {
		this.writerId = writerId;
	}

	public String getHit() {
		return hit;
	}

	public void setHit(String hit) {
		this.hit = hit;
	}

	public String getFiles() {
		return files;
	}

	public void setFiles(String files) {
		this.files = files;
	}

	public String getContent() {
		return content;
	}

	public void setContent(String content) {
		this.content = content;
	}

	@Override
	public String toString() {
		return "Notice [id=" + id + ", title=" + title + ", regdate=" + regdate + ", writerId=" + writerId + ", hit="
				+ hit + ", files=" + files + ", content=" + content + "]";
	}	
}
```

> 접근제한자 private으로 멤버 변수들을 선언해주고 생성자 함수를 통해 값을 값을 받는다.
>
> EL 언어(${})로 값을 가져올거기 때문에 get메소드가 필요하다. get메소드가 없으면 el언어로 접근을 못한다.

```java
// controller
int id = Integer.parseInt(request.getParameter("id"));
String title = rs.getString("TITLE");
Date regdate = rs.getDate("REGDATE");
String writerId = rs.getString("WRITER_ID");
String hit = rs.getString("HIT");
String files = rs.getString("FILES");
String content = rs.getString("CONTENT");

Notice notice = new Notice(id, title, regdate, writerId, hit, files, content);
request.setAttribute("n", notice);
```

> 컨트롤러에 각 변수에 대한 데이터 값을 저장하는 것은 없애고 위 처럼 변경해주면 된다.

```jsp
// detail.jsp
${n.title}
${n.regdate}
${n.files}
...
```

> 화면에 뿌려주는 페이지에서 html 코드 중간 중간에 원하는 값을 넣기 위해 EL 표현식으로 접근하면 된다.

#### 목록 페이지도 MVC model2로 만들기

컨트롤러에 NoticeListController를 만들어서 글 목록들도 mvc 모델로 구현하자.

```java
package com.newlecture.web.controller;

import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.newlecture.web.entity.Notice;

@WebServlet("/notice/list")
public class NoticeListController extends HttpServlet {
	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		List<Notice> list = new ArrayList<>();
		String url = "jdbc:oracle:thin:@localhost:1521/xepdb1";
		String sql = "SELECT * FROM NOTICE";

		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			Connection con = DriverManager.getConnection(url, "newlec", "1234");
			Statement st = con.createStatement();
			ResultSet rs = st.executeQuery(sql);
			while(rs.next()){
				int id = rs.getInt("ID");
				String title = rs.getString("TITLE");
				Date regdate = rs.getDate("REGDATE");
				String writerId = rs.getString("WRITER_ID");
				String hit = rs.getString("HIT");
				String files = rs.getString("FILES");
				String content = rs.getString("CONTENT");
				
				Notice notice = new Notice(id, title, regdate, writerId, hit, files, content);
				list.add(notice);
			}
			rs.close();
			st.close();
			con.close();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		request.setAttribute("list", list);
		request.getRequestDispatcher("/notice/list.jsp").forward(request, response);
	}
}
```

```jsp
<tbody>
<%
List<Notice> list = (List<Notice>)request.getAttribute("list");
for(Notice n : list){
	pageContext.setAttribute("n", n);
%>	
<tr>
    <td>${n.id}</td>
    <td class="title indent text-align-left"><a href="detail?id=${n.id}">${n.title}</a></td>
    <td>${n.writerId}</td>
    <td>${n.regdate}</td>
    <td>${n.hit}</td>
</tr>
<%} %>
</tbody>
```

> 컨트롤러에서 forward로 이어받은 데이터들을 request.get으로 받은 뒤 형 변환하여 리스트 형식으로
>
> 만들어준다. 바로 화면에 뿌려주는게 안되서 페이지 저장소에 저장 후 n.title 형식으로 뽑아준다.
>
> 더 나은 방법은 다음 시간에 해보자.

#### view 페이지 은닉하기

```java
request.getRequestDispatcher("/WEB-INF/view/notice/list.jsp").forward(request, response);
request.getRequestDispatcher("/WEB-INF/view/notice/detail.jsp").forward(request, response);
```

> 두 개의 컨트롤러에서 forward 하는 부분의 연결부분을 외부에서 접근할 수 없는 WEB-INF폴더 내에 위치
>
> 시킴으로써 view페이지를 은닉할 수 있다.

#### JSTL을 이용한 목록페이지 구현 (JSP Standard Tag Library)

```jsp
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<c:forEach var="n" items="${list}" varStatus="st">	// 인덱스 표시
<tr>
    <td>${st.index+1} / ${n.id}</td>	// 목록 표시 1 / 8
    <td class="title indent text-align-left"><a href="detail?id=${n.id}">${n.title}</a></td>
    <td>${n.writerId}</td>
    <td>${n.regdate}</td>
    <td>${n.hit}</td>
</tr>
</c:forEach>
```

> 먼저 jstl1.2 버전을 다운받고 WEB-INF > lib > 여기에 jstl.jar파일을 위치시켜준다.
>
> 상단 부분에 taglib 태그를 적어준 뒤 c:forEach 태그로 EL표현식으로 따온 list데이터를 pageContext.setAttribute("n", n) 에 저장되는 작업을 암묵적으로 실행해준다.

#### 중간정리

![](C:\Users\달려라\TIL\TIL\web\servlet&jsp\jsp.png)

> 중간에 application, page, session, cookie 라는 상태 저장소라는 것 또한 배웠다.

#### 페이지 처리하기

```jsp
<div>		
    <c:set var="page" value="${(param.p == null)?1:param.p}"/>
    <c:set var="startNum" value="${page-(page-1)%5}" />
    <c:set var="lastNum" value="23" />
		
    <c:if test="${startNum>1}">
        <a href="?p=${startNum-1}&t=&q=" class="btn btn-prev" >이전</a>
    </c:if>
    <c:if test="${startNum<=1}">
        <span class="btn btn-prev" onclick="alert('이전 페이지가 없습니다.');">이전</span>
    </c:if>
</div>

<ul class="-list- center">
	<c:forEach var="i" begin="0" end="4">
	<li><a class="-text- orange bold" href="?p=${startNum+i}&t=&q=" >${startNum+i}</a></li>
	</c:forEach>		
</ul>
<div>
	<c:if test="${startNum+5<lastNum}">
		<a href="?p=${startNum+5}&t=&q=" class="btn btn-next">다음</a>
	</c:if>
	<c:if test="${startNum+5>=lastNum}">
		<span class="btn btn-next" onclick="alert('다음 페이지가 없습니다.');">다음</span>
	</c:if>
</div>
```

> EL 표현식의 내장객체 param을 이용하여 p값을 요청할(get) 때 값을 저장해주는 기능을 통해
>
> 페이지 처리를 도와준다. 표현식을 잘 봐두자

#### 첨부파일 업로드

```jsp
<td colspan="3" style="text-align:left; text-indent:10px;">
<c:forTokens var="fileName" items="${n.files}" delims="," varStatus="st">
	<a href="${fileName}">${fileName}</a>
	<c:if test="${!st.last}">
	/
	</c:if>
</c:forTokens>
</td>
```

> ( !st.last ) 이 부분은 마지막이 아니라면 실행이 되게끔 해준다. Tokens에서는 구분자로 ,를 사용하여
>
> 변수 하나 하나의 이름을 fileName으로 받아주는 것이다. text-indent를 통해 들여쓰기를 했다.