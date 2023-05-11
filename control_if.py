#제어문 if
#time이 True일때 등교성공
time = True
if time:
    print("등교성공!") #time = True 이기에 if 문에서 참이 나온다
else:
    print("지각")

#time이 False라면
time = False
if time:
    print("등교성공!")
else:
    print("지각") #time = False 이기에 if 문에서 참이 나오지 않고 else에서 출력이 된다.

#time이 500이하일시 등교성공
time = 200
if time <= 500:
    print("등교성공!") # time은 200으로 500이하이기 때문에 if에서 "등교성공!"이 출력된다.
else:
    print("지각")

#time과 distance가 둘중 하나가 참일시 등교성공
distance = 50
time = 200
if time < 100 or distance <= 70:  #time은 참이 아니지만 distance가 참이기에 "등교성공!"이 출력된다.
    print("등교성공!")
else:
    print("지각")

#time과 distance가 둘다 참일시 등교성공
distance = 50
time = 200
if time < 100 or distance <= 70:  #distance가 참일지라도 time은 참이아니기에 "지각"이 출력된다. 
    print("등교성공!")
else:
    print("지각")

#box에 snack이 있으면 "배부르다"를 출력
box = {'snack', 'money', 'book'}
if 'snack' in box:
    print("배부르다") #box에 snack이 있기때문에 "배부르다"가 출력이 된다.
else:
    print("배고프다")

#조건문에서 pass
box = {'snack', 'money', 'book'}
if 'phone' in box:
    pass #조건문에서 아무것도 하지않는것을 원할때 pass를 넣는다.
else:
    print("배고프다")

#elif에 대해
box = {'snack', 'money', 'book'}
phone = True
if 'snack' in box:
    print("배부르다")
elif 'phone':     #elif는 else안에 if를 쓰는것을 하나로 묶은것이다.
    print("시켜먹어야지")
elif 'money' in box:
    print("사먹어야지")
else:
    print("배고프다")

#한줄로 작성가능하다.
box = {'snack', 'money', 'book'}
if 'snack' in box: print("배부르다")
else: print("배고프다") #이런 식으로 한줄로 줄일수 있지만 다음줄로 넘기는것이 깔끔할 수도 있다.

#조건부 표현식
score = 50
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
#조건부 표현식은 이러한 코드를 변수 = 조건문이_참인 경우의 값 if 조건문 else 조건문이 거짓인 경우의 값으로 정의한다.
message = "success" if score >= 60 else "failure"
print(message)