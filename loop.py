#반목문 while
a = 5
#while 문은 해당 조건이 참인 경우 반복해서 수행하는 함수다.
while a < 10: #조건문
    a = a + 1 #수행할 문장
    print(a)  #수행할 문장
print("\n")
# a는 5이기에 10보다 작아 1을 더한뒤 출려하여 6이나오고 이를 만복하여 a 가 9이될때 10작아 a에 1을더한뒤 10을 출력하고 그후 a는 10이기에 10보다 작지않아 반복문이 끝나게 된다.

#보조 제어문 break, continue
b = 10
while b > 1:
    b = b -1
    if b==3:
        break #(끝내기)조건문을 완전히 빠져나가는 역할을 하는 제어문이다.
    print(b)
print("\n")
b = 10
while b > 1:
    b = b -1
    if b%2 == 0:
        continue #(계속실행)조건에 맞지 않는 경우, 조건문으로 다시 돌아가는 역할을 한다.
    print(b)
print("\n")
#무한반복
c = 1
while True: #무한반복된다.
    print (c)
    c+=1
    if c == 24:
        break
while False: #실행하지 않음
    print (c)
    c+=1
    if c == 24:
        break
#문자열 출력 반복
a = 0
while a < 5: 
    a = a +1
    print("Hello")  #수행할 문장
print("\n")
#반복문 for
a = ['Jone', 'David', 'Bob']
for name in a:
    print(name)
print("\n")
a = ['David', 'Lucy', 'V']
for name in a:
    print(name)
    if name == 'Lucy':
        break #break를 써서 그 뒤로는 실행되지 않음
        print("finish")
print("\n")
for name in a:
    print(name)
else: #루프가 실행된이후 else를 실행함
    print("finish")