# Chapter03-1
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float = 10.0            # 10 == 10.0
int = 7
list = [str1, str2]
dict = {
    "name": "Machine Learning",
    "version": 2.0
}
tuple = (7, 8, 9)

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))

# 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y) : x ** y -> 2 ** 3 x^y
"""

# 정수 선언
i = 77
i2 = -14
big_int = 7777777777777777777779999999999999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 선언
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

# 실수 출력
print(f)
print(f2)
print(f3)
print(f4)

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777777777999999999999323438238
big_int2 = 28934798237489273984720384098390480923894
f1 = 1.234
f2 = 3.938

# + 
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)

# 형 변환 자동 (정수와 실수 같이 계산하면 자동으로 형이 변환)
a = 4+ 1.0
print(a)
print(type(a))

# *
print(">>>>>+")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)

# -
print(">>>>>-")
print("i1 - i2 : ", i1 - i2)
print("f1 - f2 : ", f1 - f2)
print("big_int1 - big_int2 : ", big_int1 - big_int2)

# /
print(">>>>>/")
print("i1 / i2 : ", i1 / i2)
print("f1 / f2 : ", f1 / f2)
print("big_int1 / big_int2 : ", big_int1 / big_int2)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))

"""
Traceback (most recent call last):
  File "/Users/devsisters/Desktop/Programming/python_basic/chapter03_01.py", line 120, in <module>
    print(float(b))  # 정수 -> 실수
          ^^^^^^^^
TypeError: 'float' object is not callable

어떤 객체에 이미 할당되었기 때문에 이런 에러가 발생하고 있음
"""
# 내장 함수 복원
del float
del int

# 형 변환
print(float(b))  # 정수 -> 실수
print(int(c))  # 실수 -> 정수
print(int(d))  # 실수 -> 정수
print(int(True))  # Bool -> 정수 True : 1, False : 0
print(float(True))  # Bool -> 정수
print(int(False))  # Bool -> 정수
print(float(False))  # Bool -> 정수
print(complex(3))  # 정수 -> 복소수
print(complex('3'))  # 문자 -> 복소수(숫자형)
print(complex(False))  # Bool -> 복소수

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) # x : 몫, y : 나머지

print(x, y)
print(pow(5, 3), 5 ** 3)

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 적은 정수
print(math.pi) # 원주율