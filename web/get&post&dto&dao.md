웹 컨테이너 : 웹 브라우저에서 사용자가 접속하기위해 서버에 요청을 보내고

서버는 그에 맞는 화면을 사용자에게 뿌려주는 행위를 할 수 있게 해주는 프레임워크(Tomcat 같은)

https://gmlwjd9405.github.io/2018/12/25/difference-dao-dto-entity.html

controller, service, repository(dao) 등 기초 개념 잘 나와있는 링크

https://mommoo.tistory.com/60 : 웹 기초개념 잘 나와있는 곳

DTO (data transfer object) : 계층 간 데이터 교환을 위한 객체(java beans)이다.

> DB에서 데이터를 얻어 Service나 Controller 등으로 보낼 때 사용하는 객체.

DAO (data access object) : (repository package) 실제로 DB에 접근하는 객체이다.

> 실질적으로 DB와 1:1로 연동되서 DB에 내용을 기록하고 DB에서 내용을 가져오는 역할.

> Persistence Layer(DB에 data를 CRUD하는 계층)이다.
>
> (Create Read Update Delete) SQL을 사용하여 DB에 접근한 후 적절한 CRUD API를 제공한다.

Entity Class (domain package) : 실제 DB의 테이블과 매칭될 클래스.

> 즉, 테이블과 링크될 클래스임을 나타낸다. Entity 클래스 또는 가장 Core한 클래스라고 부른다.

GET : 데이터를 가져오는 명령어

SET : 데이터를 기록하는 명령어

GET & POST METHOD : 

> 클라이언트(컴퓨터)가 서버에게 웹페이지를 보여달라고 말하는 것을 **요청**이라 부르고(접속)
>
> 서버는 클라이언트에게 **요청**받은 것에 대한 대답으로 웹페이지 내용 표현을 위해
>
> HTML문서로 주는 것을 **응답**이라 한다.

HTTP 패킷 :

> 클라이언트가 서버로 요청을 했을 때, 보내는 데이터를 HTTP패킷이라 표현한다.
>
> HTTP 프로토콜을 쓰므로, 앞에 HTTP가 붙고 인터넷을 통해 보내는 데이터를 패킷이라 표현하므로,
>
> HTTP패킷 이라 부른다. HTTP패킷의 구조는 크게 헤더와 바디로 나뉘어진다.
>
> 헤더에는 7가지 HTTP 메서드 방식 중 무엇을 썼는지, 클라이언트의 정보, 브라우저 정보,
>
> 접속할 URL 등등 과 같은 클라이언트 정보를 담는다. 바디는 보통 비어있다.
>
> 특정한 경우 데이터를 담아서 서버에 요청을 보낼 수 있다.
>
> 이러한 웹 개념아래 GET메서드와 POST메서드를 통해서 요청을 할 수 있따

'GET' VS 'POST'

> GET방식으로 데이터 보내기 >> 클라이언트의 데이터를 URL뒤에 붙여서 보낸다
>
> 만약 아이디와 패스워드를 보낸다고 하면, www.naver.com?id=jinojino&pass=1234 이런 식이다.
>
> URL 뒤에 '?' 마크를 통해 URL의 끝을 알리면서 데이터 표현의 시작점을 알린다.
>
> 데이터는 KEY와 VALUE 쌍으로 넣어야한다. 위 처럼 KEY는 id와 pass고 VALUE는 jinojino와 1234가 된다.
>
> 2개 이상 데이터를 보낼 때는 &(엔퍼센트) 이어준다(구분).
>
> URL에 붙이므로 HTTP패킷의 헤더에 포함되어 서버에 요청한다.
>
> 따라서 GET방식에서 BODY에 특별한 내용을 넣을 것이 없으므로 BODY가 빈상태로 보내진다.
>
> 그러므로 헤더의 내용 중 BODY 데이터를 설명하는 Content-Type이라는 헤더필드는 들어가지 않는다.
>
> URL형태로 표현되므로 특정 페이지를 다른사람에게 접속하게 할 수 있따.
>
> 또한 간단한 데이터를 넣도록 설계되어 데이터를 보내는 양에 한계가 있다.

> POST방식으로 데이터 보내기 : GET 방식과 달리 데이터 전송을 기반으로 한 요청 메서드이다.
>
> GET은 URL에 데이터를 붙여서 보내는 반면, POST방식은 URL이 아니고 BODY에다가 데이터를
>
> 넣어서 보낸다. 따라서 헤더필드 중 BODY의 데이터를 설명하는 Content-Type이라는 헤더 필드가
>
> 들어가고 어떤 데이터 타입인지 명시한다. 보통 BODY에 KEY와 VALUE쌍으로 데이터를 넣는다.
>
> 자바와 같이 OOP프로그래밍에서는 BODY에 데이터를 **InputStream/OutputStream** 클래스를
>
> 통해서 읽고/쓰고 한다.

GET 방식과 POST 방식에 대한 상식

>  POST방식이든 GET방식이든 보내는 데이터는 전부 클라이언트 측에서 볼 수 있따. 단지 GET방식은
>
> URL에 데이터가 표시되어 그냥 볼 수 있는거지 두 방식 모두 보안을 생각한다면 암호화를 해야한다.

GET방식이 POST방식보다 빠르다?

> 빠른건 맞다. 이유는 GET방식의 요청은 캐싱(한번 접근 후,또 요청할 시 빠르게 접근하기 위해
>
> 데이터를 저장시켜 놓는다)때문에 빠른 것이다.

URL 와 URI 의 차이점 (Uniform Resource Locater & Identifier(식별자))

> www.naver.com.preview.php 에서 문자열로 이동하는 것은 URL, 이유는 preview.php 파일을 여는 것,
>
> 위의 문자열은 특정 웹사이트로 이동되므로 URI라고 한다.
>
> URL : 파일 위치로 이동하는 경우.
>
> URI : 특정 문자열을 통해 이동하는 경우.