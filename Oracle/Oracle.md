#### Oracle

```mysql
CREATE TABLE MEMBER
(
    ID      NVARCHAR2(50),	--N은 National의 약자였나 모든 언어를 받을 수 있는.
    PWD     NVARCHAR2(50),  --NVARCHAR는 한글이든 어떤 언어든 한 글자에 2BYTE로 처리.
    NAME    NVARCHAR2(50),
    GENDER  NCHAR(2),    --남성, 여성 그냥 CHAR일 경우 한글은 3BYTE인데 1CHAR는 1BYTE이므로 오류
    AGE     NUMBER(3),
    BIRTHDAY    CHAR(10),   --2000-02-02
    PHONE   CHAR(13),   --010-1234-5678
    REGDATE DATE
);    

SELECT LENGTHB(GENDER) FROM MEMBER;
ALTER TABLE MEMBER MODIFY ID NVARCHAR2(20);
ALTER TABLE MEMBER DROP COLUMN AGE;
ALTER TABLE MEMBER ADD EMAIL VARCHAR2(200);

CREATE TABLE NOTICE
(
    ID          NUMBER,
    TITLE       NVARCHAR2(100),
    WRITER_ID   NVARCHAR2(50),
    CONTENT     CLOB,
    REGDATE     TIMESTAMP,
    HIT         NUMBER,
    FILES       NVARCHAR2(1000)
);

CREATE TABLE "COMMENT"
(
    ID          NUMBER,
    CONTENT     NVARCHAR2(2000),
    REGDATE     TIMESTAMP,
    WRITER_ID   NVARCHAR2(50),
    NOTICE_ID   NUMBER
);

CREATE TABLE ROLE
(
    ID          VARCHAR2(50),
    DISCRIPTION NVARCHAR2(500)
);

CREATE TABLE MEMBER_ROLE
(
    MEMBER_ID   NVARCHAR2(50),
    ROLE_ID     VARCHAR2(50)
);

INSERT INTO MEMBER(ID, PWD) VALUES('newlec', '111');
INSERT INTO MEMBER(ID, PWD) VALUES('dragon', '111');
SELECT * FROM MEMBER;

SELECT ID AS USER_ID, NAME, PWD FROM MEMBER;    --AS 생략 가능
DELETE FROM MEMBER WHERE NAME = 'jino'; -- from 생략 가능
DELETE FROM MEMBER WHERE GENDER = '남성';

UPDATE MEMBER SET PWD='333', NAME='손오공' WHERE ID='dragon';
DELETE MEMBER WHERE ID='test' AND PWD='111';
INSERT INTO NOTICE VALUES(1, 'JDBC란 무엇인가?', 'newlec', 'aaa', SYSDATE, 0, '');
SELECT * FROM NOTICE;
COMMIT;	--일을 마쳤으면 COMMIT으로 저장.
```

