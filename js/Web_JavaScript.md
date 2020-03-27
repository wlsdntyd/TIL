### Web JavaScript

> 최상위 객체 window 밑으로 DOM(Document Object Model) 과 BOM(Browser Obejct Model)
>
> 과 JavaScript 가 있다.

```javascript
<body>
    <p id="target">Cording everybody!</p>
    <p> data : <input type="text" id="datasource" value="JavaScript" /></p>
    <p> start : <input type="text" id="start" value="5" /></p>
    <p> end : <input type="text" id="end" value="5" /></p>
    <p><input type="button" value="appendData(data)" onclick="callAppendData()" />
    <input type="button" value="deleteData(start,end)" onclick="callDeleteData()" />
    <input type="button" value="insertData(start,end)" onclick="callInsertData()" />
    <input type="button" value="replaceData(start,end,data)" onclick="callReplaceData()" />
    <input type="button" value="substringData(start,end)" onclick="callSubstringData()" /></p>
    <script>
        var target = document.getElementById('target').firstChild;
        var data = document.getElementById('datasource');
        var start = document.getElementById('start');
        var end = document.getElementById('end');
        function callAppendData() {
            target.appendData(data.value);
        }
        function callDeleteData() {
            target.deleteData(start.value, end.value);
        }
        function callInsertData() {
            target.insertData(start.value, data.value);
        }
        function callReplaceData() {
            target.replaceData(start.value, end.value, data.value);
        }
        function callSubstringData() {
            alert(target.substringData(start.value, end.value));
        }
    </script> 
</body>
```

> 태그 접근법과 다섯 가지 함수 사용법.

```javascript
<body>
    <form id="target" action="mobiletest.html" method="post">
        <label for="name">name</label> <input id="name" type="text" />
        <input type="submit" />
    </form>
    <script>
        var t = document.getElementById('target');
        t.addEventListener('submit', function (event) {
            if (document.getElementById('name').value.length === 0) {
                alert('필드의 값이 누락되었습니다.');
                event.preventDefault();
            }
        });
    </script> 
</body>
```

> 폼에서의 값 누락 시 경고창 띄우기.