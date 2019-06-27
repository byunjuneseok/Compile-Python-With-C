# Cython

*https://cython.org/*



## What is Cython?

Cython은 C라이크한 정적 타이핑을 지원하고, C로 구현된 함수들을 바로 호출할 수 있게 해준다. `OpenMP` 를 지원하기 때문에 주로 계산 코드를 더 빠르게 변경하기 위해 사용되기도 한다. (이때 스레드는 파이썬 코드가 아니라 C코드 레벨에서 동작한다.)

*Cython을 사용하는 라이브러리로는 `scipy`, `scikit-learn`, `lxml`, `zmq`등이 있다.*



### How to use?

컴파일된 확장 모듈을 작성하는 괒엉에는 세 가지 파일이 관여한다.

* 호출하려는 파이썬 코드
* 새롭게 컴파일된 `.pyx` 파일
* 확장 모듈을 작성하기 위해 Cython 을 호출하는 과정을 포함한 `setup.py` 파일

> `setup.py` 스크립트에서 Cython을 사용해 `.pyx` 파일을 컴파일한다. 유닉스류 시스템에서는 `.so` 파일이 만들어지며 윈도우에서는 DLL과 비슷한 파이썬 라이브러리인 `.pyd`파일로 만들어진다.



## Contents

1. Hello World. [링크](./hello/README.md)

   *Work in progress.*

