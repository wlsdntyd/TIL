## MySQL Basic

- CREATE DATABASE 이름;
  - 데이타 베이스 생성
- CREATE TABLE 테이블명 ( 속성명 속성값 NOT NULL(DEFAULT.VALUE) COMMENT );
  - 테이블 추가 및 열 속성명과 속성값 지정
- ALTER TABLE 테이블명 ADD 속성명 속성값;
  - 속성 추가
- ALTER TABLE 테이블명 ADD PRIMARY KEY(속성명);
  - 테이블 생성 시 기본키 설정 놓치면 ALTER를 이용하면 된다.
- ALTER TABLE 테이블명 MODIFY 속성명 속성값;
  - 속성과 속성값 변경
- ALTER TABLE 테이블명 DROP 속성명;
  - 속성 삭제
- FOREIGN KEY(속성) REFERENCES 테이블명(속성);
  - 외래키 설정 방법.
- INSERT INTO 테이블명 (속성명1, 속성명2 ....) VALUES ('A', 'B', 'C' .....);
  - 값 추가하기.
- INSERT INTO 테이블명 VALUES('A', 'B', 'C' ......);
  - 속성명 없이 값 추가하기. 순서만 잘 맞추면 된다.
- SELECT * FROM 테이블명;
  - 해당 테이블의 모든 속성값 출력 DISTINCT사용 시 중복 튜플은 하나만 출력
- SELECT 속성명 AS 변경할 속성명 FROM 테이블;
  - AS 로써 이름바꿈
- SELECT * FROM 테이블명 WHERE 조건.

### 데이터 검색을 위한 LIKE 사용법 

1. % : 0개 이상의 문자 (내용,개수 상관없음)
2. _ : _ 개수 만큼 문자 (내용 상관없음)
3. LIKE 'AB%' : AB로 시작하는 문자열
4. LIKE '%AB' : AB로 끝나는 문자열
5. LIKE '%AB%' : AB가 포함된 문자열
6. LIKE 'AB__' : AB로 시작하는 총 네글자 문자열
7. LIKE '__A%' : 세번째 문자가 A로 시작하는 문자열
8. IS NULL : NULL 인 문자열, IS NOT NULL : NULL이 아닌 문자열

SELECT 속성명 FROM 테이블명 WHERE 조건 ORDER BY ASC/DESC(오름/내림) LIMIT ()

