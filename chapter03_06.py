# Chapter03-6
# 집합(Set) 특징
# 집함(Set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}                # 딕셔너리와 동일하게 사용하지만 차이점은 key가 없고, 리스트를 나열하듯이 선언하면 집합
f = {42, 'foo', (1, 2, 3,), 3.14159}

print('a - ', type(a), a, 2 in b)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 :', s1.intersection(s2))

# 합집합
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 :', s1.union(s2))

# 차집합
print('s1 - s2 :', s1 - s2)
print('s1 - s2 :', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 :', s1.isdisjoint(s2))       # 교집합이 있으면 False, 없으면 True

# 부분 집합 확인 (s1과 s2는 어떠한 서로 간에 한 집합의 전체가 포함되는 부분집합이 아님)
print('subset : ', s1.issubset(s2))                    # s1이 s2의 부분집합이면 True, 아니면 False
print(s2.issubset(s1))                    # s2가 s1의 부분집합이면 True, 아니면 False

s3 = set([1, 2, 3])                       # s3은 s4의 부분집합       
s4 = set([1, 2, 3, 4, 5])
print(s3.issubset(s4))                    # s3이 s4의 부분집합이면 True, 아니면 False
print(s4.issubset(s3))                    # s4가 s3의 부분집합이면 True, 아니면 False

print(s1.issuperset(s2))                  # s1이 s2를 포함하는 집합이면 True, 아니면 False
print('supertset : ', s4.issuperset(s3))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)

# 없는 원소 삭제 시 에러 발생
"""
Traceback (most recent call last):
  File "/Users/devsisters/Desktop/Programming/python_basic/chapter03_06.py", line 82, in <module>
    s1.remove(7)
KeyError: 7
"""
# s1.remove(7)

s1.discard(3)
print('s1 - ', s1)

# 없는 원소 삭제 시 에러 발생하지 않음 (예외 발생하지 않음)
s1.discard(7)

# 모두 제거
s1.clear()
print('s1 - ', s1)