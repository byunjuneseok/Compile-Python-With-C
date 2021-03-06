# C언어로 컴파일하기



## 어떤 상황에서 python을 C로 컴파일해야 하는가?

이미 최적의 알고리즘을 사용하고 있고 처리해야 할 데이터를 간소화헀다고 가정하면, 수행할 명령어의 수를 줄이는 가장 쉬운 방법은 **코드를 기계어로 컴파일하는 것**이다.



### 컴파일을 수행하는 다양한 도구들

이를 위한 방법으로는 순수 C 기반의 컴파일을 수행하는 `Cython`, `Shed Skin`, `Pythran`  이 있고, LLVM기반의 컴파일을 제공하는 `Numba` 가 있다. JIT 컴파일러 (Just in time)를 포함하는 `PyPy` 등, 컴파일하여 실행 시간을 줄일 수 있는 다양한 옵션들이 있다. 이들은 새로운 의존성 문제를 가져오며, `Cython` 를 사용하기 위해서는 C언어를 알아야한다. 팀의 생산성을 떨어뜨릴 우려가 있지만, 필요한 부분에만 잘 선택하여 이용한다면 이는 작은 문제에 불과하다.

| 방법      | 설명                                                         |
| --------- | ------------------------------------------------------------ |
| Cython    | C언어로 컴파일하기위해 가장 일반저긍로 사용되는 도구, `numpy` 와 일반 파이썬 코드를 모두 커버한다. |
| Shed Skin | `numpy`를 사용하지 않는 코드를 자동으로 C로 변환해주는 도구  |
| Numba     | `numpy`코드에 특화된 새로운 컴파일러                         |
| Pythran   | `numpy`와 비`numpy` 코드를 모두 커버하는 새로운 컴파일러     |
| PyPy      | 일반 파이썬 실행환경을 대체하는 비`numpy` 코드를 위한 JIT 컴파일러 |



### 타입정보가 실행 속도에 영향을 주는 이유

파이썬은 변수가 어떤 타입의 객체라도 참조할 수 있고, **코드 어디에서든 참조하는 객체의 타입을 변경할 수 있는 동적 언어**이다. 이런 특징으로 인해 가상머신이 다음 연산에 사용할 기본적인 타입을 알 수 없으므로 기계어 수준의 최적화를 수행하기 어렵다. 코드를 추상화할수록 실행 속도는 느려진다. [참고](./python_object.md) 



## Contents

1. [Cython](./cython)