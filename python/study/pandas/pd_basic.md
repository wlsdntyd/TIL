```python
import pandas ad pd

data = {'id': [1,2,3,4,5],		# id, pw, email의 헤더 값을 가지는 데이터 생성.
	    'pw': ['ab', 'cd', 'ef', 'gh', 'ij'],
	    'email': [a,b,c,d,f]}
f = pd.DataFrame(data)	# 구조화 시킴
f = pd.read_scv('파일이름.확장자명')
f.iloc[1,2]		# 두 번째행 세 번재열 접근
f.iloc[1,2] = 'abc'	# 값 대입
f.iloc[1,2] = f.iloc[1,2] + 'def'	# 값 변경.
f['pw'] = 'a'    # 모든 'pw'열 값 'a'로 바뀜.
f['pw'] = ['z','y','x']  # 데이터의 개수 일치 시 순서대로 대입.
f = f[['email','id','pw']]	# 헤더 값의 위치 바꿀 때 사용, 물론 데이터 같이 바뀜.
f.to_csv('./info.csv', header=True, index=False)	# 바뀐 내용 csv파일로 저장.
```

