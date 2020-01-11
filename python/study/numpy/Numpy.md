## Numpy

- 다차원 배열을 효과적으로 처리할 수 있다.
- python의 기본 list에 비해 빠르고 강력한 기능을 제공한다.
- 1차원 축(행): axis 0 => Vector
- 2차원 축(열): axis 1 => Matrix
- 3차원 축(채널): axis 2 => Tensor(3차원 이상)

```python
import numpy

list_data = [1, 2, 3]
array = numpy.array(list_data)
print(array)		# ==> [1 2 3] list일 땐 콤마가 있었는데 넘파이로 쓰니 빠졌다.
print(array.size)	# ==> 3 요소의 개수를 알려줌
print(array.dtype)	# ==> int32 타입
print(array[2])		# ==> list처럼 인덱스 번호로 접근
```

```python
import numpy as np

array1 = np.arange(4)	# 0부터 3까지 배열 만듬
print(array1)

array2 = np.zeros((4, 4), dtype=float)	# 4 * 4의 0값으로 배열 생성.
print(array2)

array3 = np.ones((3, 3), dtype=str)	# 3 * 3의 1값으로 배열 생성. 값 속성은 문자열 ('1')

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3)) # 10까지가 아니고 9까지.
print(array4)

# 평균이 0이고 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print(array5)
```

> [0 1 2 3]
> [[0. 0. 0. 0.]
>  [0. 0. 0. 0.]
>  [0. 0. 0. 0.]
>  [0. 0. 0. 0.]]
> [['1' '1' '1']
>  ['1' '1' '1']
>  ['1' '1' '1']]
> [[3 8 6]
>  [9 9 8]
>  [7 8 2]]
> [[-0.59731092  0.10412331 -1.91360817]
>  [ 1.08518973 -0.27166216  1.54793794]
>  [ 0.15236442  0.76529942  0.38752778]]

```python
import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([7, 8, 9])
array4 = np.concatenate([array1, array2, array3])	# 배열 합치는 함수
print(array4)
```

> [1 2 3 4 5 6 7 8 9]

```python
import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = array1.reshape((2, 2))		# 배열 모양 바꾸는 함수.
print(array2)
```

> [[1 2]
>  [3 4]]

```python
import numpy as np

array1 = np.arange(4).reshape(1, 4)
array2 = np.arange(8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)	# 세로(행)으로 추가 시킬 때에는
print(array3)										# axis=0 으로 맞춰준다.
```

> [[0 1 2 3]
>  [0 1 2 3]
>  [4 5 6 7]]

```python
import numpy as np

array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)	# split함수 배열을 나누는 함수
print(array)
print(left)
print(right)
```

>[[0 1 2 3]
> [4 5 6 7]]
>[[0 1]
> [4 5]]
>[[2 3]
> [6 7]]

```python
import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)
print(array * 10)	# 배열의 곱셈
```

> [[2 7]
>  [6 5]]
> [[20 70]
>  [60 50]]

![](C:\Users\달려라\Pictures\Screenshots\스크린샷(24).png)

> 배열의 연산이 이루어질 때 동적으로 행이나 열을 기준으로 넓은 배열과 형태를 맞춰 연산을 한다.

```python
import numpy as np

array1 = np.arange(8).reshape(2, 4)
array2 = np.arange(8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)
array4 = np.arange(4).reshape(4,1)
print(array3)
print(array4)
print(array3 + array4)
```

> [[0 1 2 3]
>  [4 5 6 7]
>  [0 1 2 3]
>  [4 5 6 7]]
> [[0]
>  [1]
>  [2]
>  [3]]
> [[ 0  1  2  3]
>  [ 5  6  7  8]
>  [ 2  3  4  5]
>  [ 7  8  9 10]]

```python
import numpy as np

array1 = np.arange(16).reshape(4, 4)
print(array1)

array2 = array1 < 10	# 10보다 작은 값에 True 반환.
print(array2)

array1[array2] = 100	# True로 되어 있는 곳에 100을 대입.
print(array1)
```

> [[ 0  1  2  3]
>  [ 4  5  6  7]
>  [ 8  9 10 11]
>  [12 13 14 15]]
> [[ True  True  True  True]
>  [ True  True  True  True]
>  [ True  True False False]
>  [False False False False]]
> [[100 100 100 100]
>  [100 100 100 100]
>  [100 100  10  11]
>  [ 12  13  14  15]]

```python
import numpy as np

array = np.arange(16).reshape(4, 4)

print("최대값: ", np.max(array))	# numpy 의 최대,최소값 합계,평균 구하는 함수.
print("최소값: ", np.min(array))
print("합계: ", np.sum(array))
print("평균값: ", np.mean(array))
```

> 최대값:  15
> 최소값:  0
> 합계:  120
> 평균값:  7.5

```python
import numpy as np

array = np.arange(16).reshape(4, 4)

print(array)							 # axis가 0이라면 행 기준, 1 이면 열 기준.
print("합계: ", np.sum(array, axis=0))	# 1을 넣어도 출력은 행 기준이라는 것 알아두자.
```

> [[ 0  1  2  3]
>  [ 4  5  6  7]
>  [ 8  9 10 11]
>  [12 13 14 15]]
> 합계:  [24 28 32 36]