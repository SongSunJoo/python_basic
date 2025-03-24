# Chapter02-1
# 파이썬 완전 기초
# print 사용법

"""
    참고 : Escape 코드
    
    \n : 개행
    \t : 탭
    \\ : 문자
    \' : 문자
    \" : 문자
    \000 : 널 문자
"""

# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

# 줄바꿈
print()

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
import sys
print('Learn Python', file=sys.stdout)

print()

# format 사용(d 정수 : 3, s 문자열 : 'python', f 실수 : 3.1335454)
# % 대신에 , 사용 가능
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice')) # 10자리 확보

print('%-10s' % ('nice'))
print('{:10}'.format('nice'))

print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy'))
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f
print('%1.8f' % (3.14343434343))
print('{:f}'.format(3.14343434343))

print()

print('%06.2f' % (3.14151615161717171616))
print('{:06.2f}'.format(3.14151615161717171616))