## DataBase  설계

다 대 다 관계에서는 새로운 테이블이 필요함 

일 대 다 관계에서는 다 쪽에 일이 붙음 외래키로 사용 대부분 일 대 다 경우가 많음

일 대 일 관계에서는 어느 한쪽에 붙음

```python
import pymysql

conn = None
try:
    conn = pymysql.connect(
        host = 'localhost', user = 'root', password = '1234',
        db = 'python', charset = 'utf8') # 데이터베이스 접속
    
    with conn.cursor() as cursor: # Cursor 객체 생성
        sql = '''CREATE TABLE mysql (
                ID INTEGER PRIMARY KEY AUTO_INCREMENT
                , TITLE VARCHAR(100), CONTENT VARCHAR(100))'''
        cursor.execute(sql) # SQL 실행
		conn.commit()
        
except pymysql.InternalError as e:
    print(e)
finally:
    if conn:
        conn.close()
```

> 파이썬으로 데이터베이스 접속 및 테이블 생성

```python
import pymysql

conn = pymysql.connect(
    host = 'localhost', user = 'root', password = '1234',
    db = 'python', charset = 'utf8') # 데이터베이스 접속

cursor = conn.cursor() # Cursor 객체 생성
sql = '''INSERT INTO mysql ( ID, TITLE, CONTENT)
            VALUES(NULL, %s, %s)'''	# %d 가 잘 안 먹혀서 %s로.
cursor.execute(sql, ('제목A', '내용Z')) # SQL 실행
conn.commit()
cursor.close()
conn.close()
```

> 파이썬을 이용한 sql  데이터 추가

```python
import pymysql

conn = pymysql.connect(
    host = 'localhost', user = 'root', password = '1234',
    db = 'python', charset = 'utf8') # 데이터베이스 접속

cursor = conn.cursor() # Cursor 객체 생성
sql = '''UPDATE mysql SET TITLE = %s
            WHERE ID = %s'''
cursor.execute(sql, ('제목수정됨', 1)) # SQL 실행
conn.commit()
cursor.close()
conn.close()
```

> 파이썬을 이용한 sql  데이터 수정

```PYTHON
import pymysql
conn = pymysql.connect(
    host='localhost', user='root', password='1234',
    db='pythondb', charset='utf8')
cursor = conn.cursor()
sql = '''CREATE TABLE MEMBER(
            NUM INTEGER PRIMARY KEY AUTO_INCREMENT,
            NAME VARCHAR(30),
            EMAIL VARCHAR(30),
            C_DATE DATETIME ) '''
cursor.execute(sql) # SQL 실행
conn.commit()
cursor.close()
conn.close()
```

> 선 데이터베이스 생성 후 실행, 테이블 열을 설정해줌.

```PYTHON
import pymysql
conn = pymysql.connect(
 host='localhost', user='root', password='1234',
 db='pythondb', charset='utf8')
cursor = conn.cursor()
sql = '''CREATE TABLE ARTICLE (
            ID INT PRIMARY KEY AUTO_INCREMENT,
            TITLE VARCHAR(30),
            CONTENT VARCHAR(30),
            WRITER VARCHAR(30),
            HIT INT,
            C_DATE DATETIME)'''
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()
```

