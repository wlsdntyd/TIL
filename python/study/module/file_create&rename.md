```python
PS C:\Users\달려라\Desktop\plus> ipython	# powershell로 실행. 현재 위치는 빈 폴더
In [6]: import os						  # 폴더가 1000개 주어졌을 때 한번에 바꾸는 법.

In [7]: os.listdir()	# 현재위치의 파일,폴더 이름을 리스트 형식으로 갖고 있음.
Out[7]: []				# 생성 전이라 아무것도 없음

In [9]: for i in range(1000):
   ...:     os.mkdir(f"20200127 - 복사본 ({i})")	# 폴더 1000개 생성.
   ...:

In [12]: for i in os.listdir():	# 생성된 폴더들이 반복됨.
    ...:     os.rename(i, i.replace(" ", "").replace("-", "_"))
    ...:		# 공백은 제거, 하이폰은 언더바로 변경.

In [14]: for i in os.listdir():
    ...:     os.rename(i, f"{i.split("_")[1]}_{i.split("_")[0]}")
  File "<ipython-input-14-50ed524420e4>", line 2
    os.rename(i, f"{i.split("_")[1]}_{i.split("_")[0]}")
                             ^
SyntaxError: invalid syntax	# 문자열이 입력되야하는데 문자열 안에 큰 따움표로 인해 오류.

In [15]: for i in os.listdir():
    ...:     os.rename(i, "{}_{}".format(i.split('_')[1], i.split('_')[0]))
    ...:		# 그냥 포맷팅을 바깥에서 처리.

In [16]: i
Out[16]: '20200127_복사본(999)'
```

> 폴더 이름을 한번에 만들고 변경하고 싶을 때 쓸 수 있는 방법.