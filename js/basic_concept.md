##### https://opentutorials.org/course/50 : js 함수들 사용법

```javascript
alert(1 == '1');		// true
alert(1 === '1');		// false 이것을 써야한다.
```

> ' == ' 두 개일 땐 **데이터 타입 상관없이 값만 같다면 true**
>
> ' === ' 세 개일 땐 **데이터 타입과 값 모두 같아야 true** (strict equal) 

```javascript
var a;
alert(a);	// undefined 정의되지 않은 것, 값이 없는 것.
a = null;	// null 이항 연산자를 통해 null 이라고 정의는 함.
alert(a);	// null	값이 없는 것
alert(null == undefined);	// true
alert(null === undefined);	// false
```

> null 과 undefined 차이 알아두기.

```javascript
id = prompt('input id ');	// id 입력
pw = prompt('input pw ');	// pw 입력
if((id == 'jinoo' || id == 'jinwoo' || id == 'jino') && pw === '1111' ) {
	alert('login success!');
} else {
	alert('login fail!');
};
```

> 자바와 조건문이나 논리 연산자 문법이 같다.

```javascript
<body>
    <script type="text/javascript">
        function strPrint() {
            for (var i = 0; i < 10; i++) {
                document.write('i hate sulgarge!!!<br />');
            }
        }
    </script>
</body>
```

> 자바와 다르게 자바스크립트는 변수를 적을 때 var i 라고 선언해야한다. html에서 작성하게 될 경우
>
> 줄 바꿈 태그 <br / \> 을 이용해야 한다. 함수를 정의할 땐 앞부분에 function을 입력.

```javascript
numbering = function () {
	for(var i = 0; i < 10; i++){
		document.write('hello!');
	}
}

// 함수를 정의할 때 위처럼 변수에 정의할 수도 있다. 위와 아래는 같다.
function numbering() {
	for(var i = 0; i < 10; i++){
		document.write('hello!');
	}
}

// 밑에는 익명 메소드 일회성 메소드
(function () {
	for(var i = 0; i < 10; i++){
		document.write('hello!');
	}
})();

// 배열 사용
var members = ['jino', 'jinwoo', 'jinoo'];
for(var i = 0; i < members.length; i++) {
    document.write('name : ' + members[i].toUpperCase());
    document.write('<br />');
}

// 배열 함수 push, concat, unshift, splice
var num = [1, 2, 3];
num.push(4);	// num = [1, 2, 3, 4]; 반환 값은 추가된 배열 총 길이.
num = num.concat([4, 5]);	// num = [1, 2, 3, 4, 5]; 반환 값은 추가된 배열 총 길이.
num.unshift(0);	// num = [0, 1, 2, 3, 4, 5]; 반환 값은 추가된 배열 총 길이.

// 삭제 함수 shift, pop 삭제될 원소 리턴 후 삭제.
num.shift();	// 맨 앞 원소 삭제 후 리턴(매개변수X)
num.pop();		// 맨 뒤 원소 삭제 후 리턴(매개변수X)

// 정렬 함수 sort, reverse 리턴 값은 정렬 후의 배열.
num.sort();		// 인자가 없을 시 일반적인 asc 정렬
num.reverse();	// 인자가 없을 시 일반적인 desc 정렬

// 객체(딕셔너리)와 적용(in for).
var grades = { 'jin' : 10, 'woo' : 20, 'kim' : 30 };
for(key in grades) {	// for in 문 배열에서도 사용 가능하다.
    document.write("key : " + key + "value : " + grades[key] + "<br />");
}	// grades.jin >> 10 .으로도 접근 가능하다.

// 객체 안에서의 객체와 메소드, 객체지향언어 인 이유
var names = {
            'kim': { 'jin': 5, 'eun': 10, 'dae': 3 },
            'park': { 'na': 1, 'ra': 2 },
            'nameprint': function () {
                for (var name in this.kim) {
                    console.log(name, this.kim[name]); }}}
        names.nameprint();
```

#### 모듈

```html
<script src='js/Script1.js'></script>	// js 모듈 불러오기
<script>
    names.nameprint();	// 불러오기
</script>
```

> 자주 사용되는 코드를 별도의 파일로 만들어 필요할 때 마다 재활용할 수 있다.
>
> 코드 수정 시 필요한 로직을 빠르게 찾을 수 있다.
>
> 필요한 로직만 로드해서 메모리 낭비를 줄일 수 있다.

#### API : app과 프로그래밍의 접점

> Application Programming Interface의 약자로 프로그램이 동작하는 환경을 제어하기 위해 제공되는
>
> 조작 장치이다. 이 조작 장치는 프로그래밍 언어를 통해 조작할 수 있다.

#### UI : 사용자와 시스템의 접점

> User Interface 의 약자로 

#### 간단한 정규표현식

```html
<script>
        var str = "hello world!"
        var pattern = /hello/;	// 옵션으로는 i(대소문자 구분 X)와 g(여러개 출력)가 있다.
    	// pat = /hello/ig; 대소문자 구분하지 않으면서 여러개 출력.
    	var pat = new RegExp('hello');	// 정규표현식 정의, 위와 같다.
        alert(pattern.exec(str));	// 해당하는 값 추출
        alert(pattern.test(str));	// 해당하는 값 boolean으로 출력
    	pattern.match(str);	// 해당 값 추출
    	str.replace(pattern, "HEL");	// HEL world | 문자열 바꾸는 메소드
    	// 
    	var str = "hello world!"
        var pattern = /(\w+)\s(\w+)/;	// 소괄호()로 묶어서 그룹화시켜준다
        var result = str.replace(pattern, '$2, $1');	// 그룹2, 그룹1
        console.log(result);	// world, hello! || !느낌표는 문자가 아니므로 해당X
</script>
```

#### 객체에서의 키 값 주는 방법

```javascript
var myapp = {};
myapp.cal = {
	'left' : null, 'right' : null
}	// myapp = { 'cal' : { 'left' : null, 'right' : null }}
```

> myapp = { 'cal' : { 'left' : null, 'right' : null }} || 좀 신기

#### 변수의 유효범위

> 자바스크립트는 자바와 달리 for, if, while 에서 선언된 변수(var)는 지역변수가 아니라 전역변수로서
>
> 범위를 갖는다. 바깥에서 변수 사용 시 잘 실행되는 것을 볼 수 있을 것이다.

#### 값으로서의 함수가 가능하다

```javascript
// 첫 번째 라인과 두 번째 라인은 같은 뜻. 이렇게 바깥의 함수는 함수라 부른다
var fn = function () {}
function fn() { }
// 
var fns = {	// 객체 안의 함수는 메소드라고 부른다.
    'a': function () {
        return true;
    }}
```

