# Python3 : 파이썬 변수에 대한 알쓴신잡 (알아두면 쓸데많은 신기한 잡학사전)

*Juneseok Byun, 2019.06*

## Python3 에서는 모든 변수가 객체 (object)

### C vs Python

```C
/* C code */
int a = 1;
int b = 2;
int c = a + b;
```

C 컴파일러는 아래와 같이 작동하게 됩니다.

1. int 4바이트 만큼의 메모리를 할당하고 a라는 이름을 붙인다 (컴퓨터는 a를 방금 할당한 메모리의 주소로 기억한다.)
2. 변수 `a` 자리에 `1`을 저장한다. (0x5의 형태로 4바이트만큼 사용할 것이다.)
3. int 4바이트 만큼의 메모리를 다시 할당하고 b라는 이름을 붙인다.
4. 변수 `b` 자리에 `2`를 저장한다. (0x5의 형태로 4바이트만큼 사용할 것이다.)
5. `binary_add<int, int>(a, b)` 를 호출한다.
6. int 4바이트 만큼의 메모리를 다시 할당하고 c라는 이름을 붙인다.
7. 호출한 함수의 결과값을 `c` 에 저장하게 된다.



위 C코드와 같은 일을 하는 파이썬 코드입니다.

```python
# python code
a = 1
b = 2
c = a + b
```

파이썬3의 인터프리터는 아래와 같이 작동하게 됩니다.

1. `1` 을  `a` 에 할당합니다.
   - **1a.** `a->PyObject_HEAD->typecode` 를 정수로 지정합니다.
   - **1b.**  `a->val = 1`
2.  `2` 를  `b` 에 할당합니다.
   - **2a.** `b->PyObject_HEAD->typecode` 를 정수로 지정합니다.
   - **2b.**  `b->val = 2`
3.  `binary_add(a, b)` 를 호출합니다.
   - **3a.**  `a->PyObject_HEAD` 안의 `typecode` 를 찾습니다.
   - **3b.** `a` 가 정수이면 값은 `a->val`
   - **3c.** `b->PyObject_HEAD` 안의 `typecode` 를 찾습니다.
   - **3d.** `b` 가 정수이면 값은 `b->val`
   - **3e.** `binary_add<int, int>(a->val, b->val)` 을 호출합니다.
   - **3f.** 결과는 `result` 이며, 정수입니다.
4. 파이썬 객체 `c` 를 생성합니다.
   - **4a.**  `c->PyObject_HEAD->typecode` 를 정수로 지정합니다.
   - **4b.**  `c->val` 을`result` 로 합니다.

파이썬은 객체의 타입을 명시적으로 지정하지 않고, **런타임에서 객체의 타입을 설정하도록 하는 동적 타이핑(Dynamic typing)**을 보여주고 있습니다. 이런 이유로 파이썬은 정적 언어인 C와 달리 **몇 가지 일들이 더 일어나게 됩니다.** 같은 일을 하더라도 C가 파이썬보다 성능 상 우위에 있음을 알 수 있습니다. 그래도 사람들이 파이썬을 쓰는 이유는 성능과 트레이드오프(Trade-off)할 수 있는 강력한 장점들(편의성, 성숙한 써드파티 라이브러리들 등)이 있기 때문입니다.



### 넘파이 vs 파이썬 `list`

![array_vs_list](assets/array_vs_list.png)

> *([http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/](http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/) 에서 발췌한 그래프입니다.)*

넘파이를 사용하는 가장 큰 이유는 메모리를 훨씬 더 효율적으로 사용하기 때문입니다.



#### (참고) 메모리 관리 원칙

- 메모리 관리의 주체는 운영체제입니다.
- 운영체제는 메모리가 있는 한은 할당 요청을 거절하지 않습니다.
- 한 번 할당된 메모리 공간은 절대로 다른 목적을 위해 재할당되지 않습니다.
- 응용 프로그램이 할당된 메모리를 해제하면 운영체제는 이 공간을 빈 영역으로 인식하고 다른 목적을 위해 사용할 수 있도록 합니다.



### `id()` 메소드

```python
id(object)
```

**객체의 아이덴티티**를 리턴해줍니다. 객체의 수명동안 유일하고 바뀌지 않음이 보장되는 정수입니다. 

> **CPython implementation detail**: This is the address of the object in memory.



### 값의 비교

```python
# 100
x = 100
y = 100
print(id(x), id(y)) # 4559940832 4559940832
print(x is y)				# True
print(x == y)				# True
print(id(100)) 			# 4559940832

# 200
x += 100
y += 100
print(id(x), id(y)) # 4559940832 4559940832
print(x is y)				# True
print(x == y)				# True
print(id(200)) 			# 4559940832

# 300 ([-5, 256] 바깥의 범위)
x += 100
y += 100
print(id(x), id(y)) # 4608180016 4608179952
print(x is y)				# False
print(x == y)				# True
id(300)							# 4612495024
```

>  정수 객체 (`int` object ) 중 [-5, 256] 범위 내의 값을 가진 객체는 이미 만들진 객체를 참조하게 됩니다. 그 밖의 값을 갖는 경우 새로운 객체를 만들어서 참조하게 됩니다.

파이썬의 `==` 와 `is` 는 비슷해보이지만, 다른 행동을 하는 연산자입니다. `==` 는 객체의 값을 비교하는 연산자이며, `is`는 객체의 참조 (아이덴티티)를 비교하는 연산자입니다. -5부터 256의 범위 안에 있는 정수의 값을 갖는 객체는 처음에 이미 만들어진 유일한 같은 객체를 참조하게 됩니다. 그러나 그 범위를 벗어나게 되면 각각 새로운 객체를 만들어 참조하게 됩니다. 

파이썬은 왜 이렇게 행동하는지, 아래의 개념을 통해 알 수 있습니다.



### immutable한 자료형, mutable한 자료형

| data type | -         |
| --------- | --------- |
| Number    | immutable |
| String    | immutable |
| Tuple     | immutable |
| List      | mutable   |
| Dict      | mutable   |

파이썬은 변수를 immutable, mutable 변수형으로 나눌 수 있습니다. 

* immutable : 객체를 생성한 후 객체의 값을 수정할 수 없다.
* mutable : 객체를 생성한 후 객체의 값을 수정할 수 있다.

이를 통해 위의 `id(x)` 와 `id(y)`의 값이 계속 바뀌는 지 알 수 있습니다. 



#### (참고) 파이썬의 리터럴

| 리터럴 유형   | -                                                            |
| ------------- | ------------------------------------------------------------ |
| 숫자 리터럴   | 정수 리터럴, 실수 리터럴, 복소수 리터럴                      |
| 문자 리터럴   |                                                              |
| 논리값 리터럴 | `True`, `False`                                              |
| 특수 리터럴   | `None`                                                       |
| 컬렉션 리터럴 | 리스트(`[ … ]`), 튜플(`( … )`), 딕셔너리(`{key : value, …}`), 셋(`{…}`) |



## Call by what?

지금까지의 내용을 이해했다면, 파이썬이 어떤 방식으로 함수에 인수를 전달하는지에 대해 쉽고 명확하게 이해할 수 있습니다. 파이썬은 **"Call by object reference"** 입니다.



## 참조
[ Python 공식문서 내장함수]: https://docs.python.org/ko/3/library/functions.html#id
[ 모호한 파이썬 튜토리얼, Call by what?]:  https://item4.github.io/2015-07-18/Some-Ambiguousness-in-Python-Tutorial-Call-by-What/
[기초 파이썬 파이썬의 모든 것은 Object이다 (정수편)]: https://ahracho.github.io/posts/python/2017-05-01-everything-in-python-is-object-integer/
[Why Python is Slow: Looking Under the Hood]:http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/

