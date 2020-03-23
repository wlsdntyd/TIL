```html
<script src="js/jquery.js"></script>	// 제이쿼리 홈페이지에서 소스 따오기
<body>
    <ul id="list">
        <li>kimjinwoo</li>
        <li>kimjinwoo</li>
        <li>kimjinwoo</li>
        <li>kimjinwoo</li>
    </ul>
    <input type="button" value="execute" id="execute_btn" />

    <script>
        $('#execute_btn').click(function () {
            $('#list li').text('hello world!');
        })
    </script>  
</body>
```

> jQuery : javascript 코드들의 집합.