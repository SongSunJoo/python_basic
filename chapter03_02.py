# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

# 형 타입
print(type(str1), type(str2), type(str3), type(str4))

# 문자열 길이
print(len(str1), len(str2), len(str3), len(str4))

# 빈 문자열
str1_t1 = '' # = ""
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문 사용
""" 참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""
# I'm Boy
print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')

print('a \t b')
print('a \n b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test'
print(raw_s)
print()

# 멀티라인 입력
multi_str = \
'''
문자열
멀티라인 입력
테스트
'''
print(multi_str)

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple!"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)    # str_o1에 y가 있나요? -> 있으면 True, 없으면 False
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수 (upper, isalnum, startswith, count, endswith, isalpha...)
print("Capitalize: ", str_o1.capitalize())      # 첫글자 대문자
print("endswith?: ", str_o2.endswith("!"))      # 끝글자가 있는지 확인
print("relplace: ", str_o1.replace("thon", 'Good'))     # 문자 변경
print("sorted: ", sorted(str_o1))               # list 형태로 반환하며, 순서가 정렬되어 노출
print("split: ", str_o4.split(' '))             # 공백 쪼개서 분리 (띄어쓰기에서 쪼개짐)

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str))              # __iter__가 있으면 반복이 가능

# 출력
for i in im_str:
    print(i)
    
# 슬라이싱
str_sl = "Nice Python"
print(len(str_sl))

# 슬라이싱 연습
print(str_sl[0:3])              # 3-1 -> 0 1 2
print(str_sl[5:])               # [5:11]
print(str_sl[:len(str_sl)])     # str_sl[:11]
print(str_sl[:len(str_sl)-1])   # str_sl[:10]
print(str_sl[1:9:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])

# 아스키 코드 (또는 유니코드)
a = 'z'

print(ord(a))               # 아스키 코드로
print(chr(122))             # 문자로