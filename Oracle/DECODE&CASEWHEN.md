#### DECODE & CASE WHEN

```mariadb
SELECT GENDER
	, DECODE(GENDER, 'M', '남자', 'F', '여자', '기타') GENDER2
	FROM TEMP
```

> if(GENDER == 'M') return '남자', else if(GENDER == 'F') return '여자', else return '기타'

```mariadb
SELECT DISTINCT GENDER,
	CASE WHEN GENDER = '001' THEN '여' ELSE '남' END AS 성별
	FROM MY_TABLE
```

> 조건이 하나 일 경우

```mariadb
SELECT *,
	(CASE WHEN SCORE >= '90' THEN 'A학점'
		WHEN (SCORE >= '80' AND SCORE < '90') THEN 'B학점'
		WHEN (SCORE >= '70' AND SCORE < '80') THEN 'C학점'
		WHEN (SCORE >= '60' AND SCORE < '70') THEN 'D학점'
		ELSE 'F학점'
	END) AS '학점'
FROM MY_TABLE
```

> 다중 조건 처리