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
> 범위를 갖는다. 바깥에서 변수 사용 시 잘 실행되는 것을 볼 수 있을 것이다. **함수 안에서의 선언된 변수는**
>
> **지역변수로서의 범위를 갖는다.**

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

#### CallBack(called at the back)

```javascript
var numbers = [20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
var sortfunc = function (a, b) {	// callback 함수
	if (a > b)
		return 1;
	else if (b > a)
		return -1;
	else return 0;
}	// 사실 다 필요없고 return a-b; 로 적으면 된다, 역순을 원하면 return b-a;
numbers.sort(sortfunc);
console.log(numbers);
```

> 정렬 메소드 sort 안에 callback 함수가 들어가면서 sort 메소드 수행 시 sortfunc 함수를 수행해야 하므로
>
> sortfunc 함수로 이동한다. 이런 과정을 CallBack이라 보면 된다.

#### 비동기(Asynchronous) < - > 동기(Synchronous)

> **동기적 방식 : 실행 순서가 확실한 것, 동시에 처리가 안 되는 것.**
>
> **비동기적 방식 : 실행 순서가 정해져있지 않은 것, 동시에 처리가 가능하다는 것.**
>
> 콜백은 비동기처리에서도 유용하게 사용된다. 시간이 오래걸리는 작업이 있을 경우 이 작업이 완료된 후
>
> 처리해야 할 일을 콜백으로 지정하면 해당 작업이 끝났을 때 미리 등록한 작업(콜백으로 지정한 작업)을
>
> 실행하도록 할 수 있다. 한 예로 ajax(asynchronous javascript and xml) 여기서 xml은 그다지,,, 안 중요
>
> 이 부분은 Ajax 를 공부해야 더 확실히 이해가 갈 것 같다.

#### Closure

> 클로저란 내부함수는 외부함수의 지역변수에 접근할 수 있는데 외부함수의 실행이 끝나서 외부함수가
>
> 소멸되도 내부함수가 외부함수의 변수에 접근할 수 있는 것이다. 밑에 코드를 보며 이해하자.

```javascript
function factory_movie(title) {	// title 매개변수로 받지만 외부함수의 지역변수로 쓰임
    return {
        get_title : function () {
            return title;
		},
		set_title: function (_title) {
			title = _title;
		}
	}
}
ghost = factory_movie('ghost in the shell');
matrix = factory_movie('matrix');
alert(ghost.get_title());		// ghost in the shell
alert(matrix.get_title());		// matrix
// 밑 코드는 메소드를 통해 값을 바꾸면서 외부함수의 지역변수 title의 값을 바꾸게 된다.
ghost.set_title('starlight');
alert(ghost.get_title());		// starlight
```

> 클로저를 이해하기에 충분한 코드같지만 하나의 예를 더 보자.

```javascript
var arr = [];
for (var i = 0; i < 5; i++) {
	arr[i] = function () {
		return i;
	}
}

for (var index in arr) {
    console.log(arr[index]());
}
```

> 위 코드는 실행시켜보면 알겠지만 5가 다섯번 출력된다.
>
> **반복문에서 클로저 사용 시 반복문이 끝날 시점의 값이 클로저가 된다.** 고로 밑 코드처럼 바꿔야한다.

```javascript
var arr = [];
for (var i = 0; i < 5; i++) {
	arr[i] = function (id) {
		return function () {
    		return id;
    }(i);
}
for (var index in arr) {
    console.log(arr[index]);
}
```

> 즉 실행함수를 만들어서 for문이 실행될 때 익명함수도 실행되도록 하면 된다.
>
> 그리고 굳이 외부 함수를 안 써도 된다.

```javascript
var arr = [];
for (var i = 0; i < 5; i++) {
	arr[i] = (function (i) {
    	return i;
    })(i);
}
```

> 함수 하나로도 충분히 실행할 수 있다.

#### Arguments : 인자 값들

```javascript
var _sum = 0;
function sum() {
	for (var i = 0; i < arguments.length; i++)
		_sum += arguments[i];
	console.log(_sum);
}
sum(1, 2, 3, 4, 5);	// 15
```

> 다른 언어들과 다르게 자바스크립트는 매개변수가 없는 함수를 호출할 때 인자 값을 넣어줘도 오류가
>
> 나지 않는다. 반대로 매개변수가 있는 함수를 호출할 때 인자 값을 안 넣어줘도 오류가 나지 않는다.
>
> 그리고 전자의 경우 인자값들을 대체할 수 있는 것이 arguments 이다. 위 코드를 잘 봐두자.

```javascript
function one(arg1) {
	console.log(one.length);		// 1
    console.log(arguments.length);	// 2
}
one(1, 2);
```

> arguments 는 함수의 매개변수와 상관없이 인자로 들어오는 갯수 전체를 가지게 된다.

#### Apply 메소드

```javascript
function sum() {
	var _sum = 0;
	for (name in this)	// apply 메소드 호출 시 인자 값의 객체가 this에 해당한다.
		_sum += this[name];
	return _sum;
}
var o = [1, 2, 3];
o1 = { val1: 1, val2: 2, val3: 3 };
o2 = { v1: 10, v2: 50, v3: 100, v4: 25 };

alert(sum.apply(o));	// 6
alert(sum.apply(o1));	// 6
alert(sum.apply(o2));	// 185
```

> 더하려는 값이 엄청 많을 경우 배열이나 객체로 정의하여 apply 메소드를 통해 값을 다 더할 수 있다.

#### 객체지향 프로그래밍(Object Oriented Programming)

#### 생성자와 new

```javascript
function person() { };
var p = new person();
p.name = 'jino';
p.introduce = function () { return ('name is ' + this.name) };
```

```javascript
function Person(name) {
    this.name = name;
    this.introduce = function () {
        console.log('name is ' + this.name);
	}
}

var p1 = new Person('jinwoo');
var p2 = new Person('eunchong');
p1.introduce();
p2.introduce();
window.p1.introduce();	// 밑 개념인 전역객체인 window를 적어보았다.
```

> 위 코드도 정상 실행되지만 하나의 객체를 만들 때 마다 name과 introduce 메소드를 적어줘야 하므로
>
> 비효율적이다. 밑에 처럼 생성자 함수를 통해 객체를 생성하는 것이 코드의 중복도 줄이고 효율적이라
>
> 볼 수 있다

#### 전역객체 (웹:window, 노드js:global)

> 코드는 바로 위의 window 를 보면 된다. 결론은 결국 p1 이나 p2 객체 또한 window의 속성이 되는
>
> 것이다. window 를 생략한거나 적은 거나 차이가 없다고 보면 된다. window. 을 적어보면 다양한
>
> 메소드들을 볼 수 있다.

```javascript
function equal() {
	if (window === this)
		console.log(true);
}
window.equal();	// true
```

> if 문이 정상실행되어 저 문장이 잘 출력되는 것을 볼 수 있을 것이다. this에 대해 헷갈리지 말자.

```javascript
var Person = {
	equal: function () {
    	if (Person === this)
        	console.log(true);
    }
}
Person.equal();	// true
```

> 객체 안의 메소드일 경우 this 는 Person을 가리킨다. 즉 this는 자신이 속해있는 전역객체를 의미한다.
>
> 밑의 마지막 예를 보면서 확실히 다져두자.

```javascript
var funcThis = null;

function Func() {
	funcThis = this;
}

var o1 = Func();
if (funcThis === window)
	document.write('window </br>');	// 정상 실행

var o2 = new Func();
if (funcThis === o2)
	document.write('o2 </br>');		// 정상 실행
```

> 생성자 함수를 통해 객체를 생성할 때와 그냥 함수로 쓸 때 this가 가리키는 것이 변하는 것을 알아두자.

#### 함수가 객체인 이유

```javascript
var o1 = new Object();	// 객체 리터럴(객체)
var o2 = {};

var a1 = new Array();	// 배열 리터럴(객체)
var a2 = [];

var sum1 = new Function ('x','y','return x+y;');	// 함수 리터럴(객체)
var sum2 = function (x, y) { return x + y; }
```

> 함수 또한 생성자를 통해 만들어진다. 고로 함수도 객체이다.

#### Apply 의 추가 설명

```javascript
var o = {'a':10, 'b':20};
var a = {};
function sum() {
	var _sum = 0;
	for(key in this)
		_sum += this[key];
	return _sum;
}
sum();	// 이때 this는 window
sum.apply(o);	// 30 이때 this는 o
sum.apply(a);	// 이때 this는 a
```

> apply를 써야 객체에서의 접근이 가능하다.

#### 상속(inherit), Prototype, Chain

```javascript
function Computer(name) {
	this.name = name;
    this.n = 10;
	this.namept = function () { console.log('name : ' + name) };
}
Computer.prototype.price = function () { console.log('10000 dollar'); }
Computer.lg = function () { console.log(true); }	// prototype 지정 안해줘서 오류남.

Notebook.prototype = new Computer(name);	// 상속을 생성자 안에서 해봤는데 안 됨.
function Notebook(name) {
    this.name = name;	// 없어도 된다.
	this.pt = function () { console.log("i'm notebook!") };
}
var c1 = new Computer('jin');
var n1 = new Notebook('jino');

n1.namept();
n1.price();
console.log(n1.n)	// 셋 다 정상 실행
```

> 자바와 다르게 생성자 안에서 상속을 못 받는 부분이 아쉽다. 내가 아직 방법을 모르는 걸 수도 있는데,,
>
> 어쨋든 JS에선 바깥에서 prototype을 지정해서 상속을 해야한다. 바깥 부분에서 prototype을 이용한
>
> 메소드 추가하는 부분도 잘 봐두자. 아 chain은 상속이 여러번 이루어 질 때 계속해서 자식이 물려받기 때문에
>
> chain이란 이름이 붙은 것 같다.

#### 표준 내장 객체(Standard Built-in Object)

> 자바 스크립트가 기본적으로 가지고 있는 객체들을 의미한다.
>
> Object, Function, Array, String, Boolean, Number, Math, Date, RegExp 가 끝이다.
>
> 호스트환경이 제공하는 api를 따로 배워야 할 것이다. 보통 웹이나 node.js 같은?

#### 배열의 확장

```javascript
var arr = new Array('seoul', 'new york', 'ladarkh', 'pusan', 'Tsukuba');

function getRandomValueFromArray(array) {
	var index = Math.floor(array.length * Math.random());	// floor는 소수점 이하 제거
	return array[index];
}
console.log(getRandomValueFromArray(arr));
Array.prototype.getRandomValue = function () {
	var index = Math.floor(this.length * Math.random());
	return this[index];
}
console.log(arr.getRandomValue());
```

> Array.prototype 을 통해서 Array객체의 메소드를 확장할 수 있다. 만약 Array.prototype이 아닌 최상위 객체
>
> Object를 확장한다면 여러 객체에서 접근할 수 있다. (Object.prototype ... )

```javascript
Object.prototype.contain = function (val) {
	for (var key in this)
		if (this[key] === val)
			return true;
	return false;
}

var o = { 'name': 'egoing', 'city': 'seoul' };
var a = ['egoing', 'leezche', 'grapittie'];
console.log(o.contain('seoul'));
```

> 위 코드는 정상적으로 실행이 되지만 최상위 객체 Object를 확장시켰으므로 위에서 정의한 객체 o 나 a 에도
>
> contain이라는 메소드가 존재하게 된다. 즉 불필요한 확장이 이루어졌으므로 위험성이 많다.
>
> 확장을 해야할 상황이 온다면 최소한의 확장으로 위험성을 줄일 필요가 있다.

#### 기본 데이터 타입과 래퍼(wrapper) 객체

숫자 --> Number(객체)

문자열 --> String(객체)

불리언 --> Boolean(객체)

null --> X

undefined --> X

> 기본 데이터 타입을 객체화시켜 객체로서의 접근을 가능하게 해준다. (ex. name.toString() )

#### 복제와 참조 and 함수

```javascript
var a = 10;
function rep(b) {   // b = a; 기본 타입이므로 값만 복제.
	b = 5;          // b = 10이 되었지만 b = 5 로 인해 b = 5가 맞음
}
console.log(a);		// 10
```

> 위의 동작원리는 굉장히 중요하다. 까먹지말자,,

```javascript
var a = { 'age': 10 };
function rep(b) {			// b = a; 객체이므로 주소 값을 가진다. 즉 참조.
	b = { 'age': 20 };		// 새로 만든 객체의 주소를 b에 넣는다.
}
console.log(a);	// {'age':10}
```

> 객체는 주소 값을 가진다는 것을 알아두자.