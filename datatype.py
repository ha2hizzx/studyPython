#정수형 
a = 123
print(a)
a = -123 #음수도 출력이 가능하다.
print(a)
#어떤형인지를 알수있다.
print(type(a)) #int는 정수형
a = 1.23
print(a) #소수도 출력이 가능하다.
print(type(a))#float은 실수형
#8진수
a = 0o177 #8진수를 만들기 위해서는 '0o'또는 '0O'로 시작하면된다.
print(a)
#16진수
a = 0x8ff #16진수로 만들기 위해서는 '0x'로 시작하면된다.
print(a)
#연산자
a = 3
b = 4
print(a + b) #더하기 3 + 4 = 7
print(a * b) #곱하기 3 * 4 = 12
print(a / b) #나누기 3 / 4 = 0.75
print(a // b) #나누기(몫) 3 // 4 = 0
print(a ** b) #제곱 3 ** 4 = 81
print(a % b) #나누기(나머지) 3 % 4 = 3
