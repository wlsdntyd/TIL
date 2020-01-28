alter add 

like %데이터 : 데이터로 끝나는

like %데이터% : 데이터 문자열을 포함하는

insert into 테이블명(속성) values (속성 값 ......)

order by  asc / desc (오름/내림차순)

select 속성 from 테이블명 where 조건

select 그룹속성,count(*) as 명칭 from 테이블명 group by 속성 having 조건(count(1) >= 3)

join : 여러 테이블을 하나로 합쳐줄 때

select 속성 from 테이블1 join 테이블2 on  테이블1.속성 = 테이블2.속성

​	join 테이블3 on 테이블1.속성 = 테이블3.속성

update 테이블명 set 속성명 = 속성값 where 조건

update 제품 set 제품명 = '통큰파이'  where 제품번호 = 'p03';

DELETE FROM 테이블명 WHERE 조건 : 조건이 없으면 전부 다 삭제됨.

EXERD :

빨간 줄 : 비식별관계 (외래키, 일 대 다) 식별 관계이기도 하다.

녹색 줄 :  식별관계 (일 대 일)

```python
import pymysql
conn = pymysql.connect(
 host='localhost', user='root', password='1234',
 db='mydb', charset='utf8')

cursor = conn.cursor(pymysql.cursors.DictCursor)	# 딕셔너리 형태화
sql = '''SELECT id, year, area1, count(*) as cnt FROM accident
            GROUP BY AREA1, YEAR'''
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row['area1'], row['year'], row['cnt'])
conn.commit()
cursor.close()
conn.close()
```

> 기존의 튜플이 아닌 딕셔너리 형태로 불어옴으로서 키 값으로 조회가 가능하다.

```python
import pymysql

page_num = int(input("원하는 페이지 번호를 입력해주세요 : "))
end_num = page_num * 10
start_num = end_num - 9

conn = pymysql.connect(
    host = 'localhost', user = 'root', password = '1234',
    db = 'mydb', charset = 'utf8') # 데이터베이스 접속

cursor = conn.cursor(pymysql.cursors.DictCursor) # Cursor 객체 생성
sql = '''SELECT * FROM EMP
            LIMIT %s, 10'''
cursor.execute(sql, (start_num - 1)) # SQL 실행
result = cursor.fetchall()

print(len(result))
for row in result:
    print(row['EMPNO'],row['ENAME'])

conn.commit()
cursor.close()
conn.close()
```

```python
import pymysql
import re

conn = pymysql.connect(
host='localhost', user='root', password='1234',
db='pythondb', charset='utf8')
cursor = conn.cursor()
sql = """SELECT ID, NAME, PERSON_NUMBER
            FROM info"""

cursor.execute(sql)
result = cursor.fetchall()
pat = re.compile('(\d{6})-\d{7}')
for row in result:		# 보여줄 부분은 반드시 그룹화를 해줘야함.
    print(row[2][:row[2].find('-')] + '-' + '*'*7) # [2][:5] >> 세번째에서 4번째 
    print(row[0], row[1], pat.sub('\g<1>*******', row[2]))	# 까지 보여줌

conn.commit()
cursor.close()
conn.close()
#########################
751111-*******
a 일길동 751111*******
761111-*******
b 이길동 761111*******
771111-*******
c 삼길동 771111*******
781111-*******
d 사길동 781111*******
791111-*******
e 오길동 791111*******
801111-*******
f 육길동 801111*******
811111-*******
g 칠길동 811111*******
```

```python
import pymysql

conn = pymysql.connect(
host='localhost', user='root', password='1234',
db='pythondb', charset='utf8')
cursor = conn.cursor()
sql = """SELECT shop_id,shop_name,shop_desc,rest_date,parking_info
            FROM shop
            WHERE rest_date = %s AND parking_info = %s
            ORDER BY shop_id desc;"""

cursor.execute(sql, ("연중무휴","주차가능"))
result = cursor.fetchall()
for i in result:	# 튜플 안에 튜플을 반복
    for j in i:
        print(j, end=" ")
    print("")
conn.commit()
cursor.close()
conn.close()
```

