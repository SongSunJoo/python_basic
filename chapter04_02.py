# Chapter04-2
# 파이썬 반복문
# FOR 실습

# 코딩의 실습
# for in <collection>
#   <Loop body>

for v1 in range(10):    # 0 ~ 9
    print('v1 is : ', v1)

print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is : ', v2)
    
print()

for v3 in range(1, 11, 2): # 1, 3, 5, 7, 9
    print('v3 is : ', v3)
    
print()

# 1 ~ 1000 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v   # sum1 = sum1 + v
    
print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum : ', sum(range(1, 1001)))

print(type(range(1, 1001)))

print('4 ~ 1000 4의 배수의 합', sum(range(4, 1001, 4)))

print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are : ', n)
    
print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current Number : ", n)

print()

# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)

# 예제4
my_info = {
    "name": "Lee",
    "age": 33,
    "city": "Seoul"
}

for key in my_info:
    print('key0 : ', key)
    print('key1 : ', my_info[key])
    print('key2 : ', my_info.get(key))
    
for v in my_info.values():
    print('value : ', v)
    
    
# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
        
# break : 바로 빠져나감
numbers = [14, 3, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print("34를 찾았어요 ", num)
        break
    else:
        print("아직 숫자를 찾지 못했어요 ", num)
        
# continue
lt = ["1", 2, 5, True, 4.3, complex(4)] # complete 복소수

for v in lt:
    if type(v) is bool:
        continue
    print("current type:", v, type(v))
    print("multiply by 2", v * 3)
    print(True * 3)