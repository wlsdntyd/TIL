## INSERT

INTO 의 속성과 VALUES 속성은 순서대로 1:1 대응을 이루어야 함.

- INSERT INTO 테이블명 (속성 리스트) VALUES (속성의 값 리스트);

  

## SELECT

- SUBSTR(대상 문자열, 시작 위치, 추출 개수) : 문자열 추출

- CONCAT(문자열1, 문자열2) : 문자열 합치기 (보통 문자열1에는 COLUMN)

- DATE_FORMAT(날짜, 출력형식) : 날짜 함수에는 NOW(), E_DATE()이 있다. 

  년:%Y 월:%m 일:%d 시간:%H 분:%i 초:%s

- CASE WHEN (속성명: 조건) THEN '새로운 속성명' WHEN () THEN .... END : 

  기존 속성명을 새로운 속성명으로 출력할 수 있다.

- GROUP BY 속성 리스트 [HAVING 조건] : 그룹화 시켜줌

- SELECT [DISTINCT] 속성 리스트 

- FROM 테이블 리스트

- WHERE 조건 

- GROUP BY 속성 리스트 HAVING 조건 

- ORDER BY 속성 리시트 [ASC|DESC]

- **JOIN** : 여러개의 테이블을 연결해 하나의 테이블처럼 사용하는 것

  - 일반적으로 외래키가 조인 속성으로 사용

| SELECT 속성                     | SELECT 속성                        |
| ------------------------------- | :--------------------------------- |
| FROM 테이블1                    | FROM 테이블1, 테이블2              |
| JOIN 테이블2                    | WHERE 테이블1.속성 = 테이블2.속성; |
| ON 테이블1.속성 = 테이블2.속성  |                                    |
| JOIN 테이블3                    |                                    |
| ON 테이블1.속성 = 테이블3.속성; |                                    |

