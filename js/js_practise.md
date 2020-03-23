```javascript
function myappfn() {
    var myapp = {};
    myapp.cal = {
        'left': null,
        'right': null
    }
    myapp.cal.left = 10;
    myapp.cal.right = 20;
    function sum() {
        return myapp.cal.left + myapp.cal.right;
    }
    document.write(sum());
}
myappfn();
```

> 객체 생성 후 cal을 붙이는 모습. 키 값으로 쓰인다고 보면 된다.

```javascript
var cal = function (func, num) { return func(num); }
var increase = function (num) { return num + 1; }
var descend = function (num) { return num - 1; }

console.log(cal(increase, 5));	// 6
console.log(cal(descend, 5));	// 4
```

> 값으로서의 함수가 가능하니 매개변수에 함수를 넣어 해당 함수에 대한 인자 값을 처리한 값을
>
> 리턴받는 구조가 가능하다. 매우 유용하게 쓰일 것 같다.