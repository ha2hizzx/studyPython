#list 만들기
arr = [] # 비어있는 리스트
arr = list()

#리스트 인덱스
arr = ['a', 'b', 'c']
print(arr)
print(arr[0])#리스트 0번째의 'a'출력 0번부터 시작
print(arr[1])#리스트 1번째의 'b'출력
print(arr[2])#리스트 2번째의 'c'출력
print(arr[-1])#-1번째 출력 'c'출력
print(arr[2:])#리스트의 2번째요소부터 끝까지
print(arr[1] + arr[2] + arr[0]) #요소 합치기
print(arr[:1])#리트의 첫번째 요소부터 1번째 요소까지
print(arr.index('c')) #'c'가 arr리스트의 몇번째에 있는지 알수있다.
arr.append('f') #'f'가 arr리스트에 추가된다.
arr.insert(1,'b2') #1번째에 'b2'를 넣는다 원레 1번째에 있던 값과 그 뒤의 값들은 뒤로 밀려난다.
arr.remove('c') # 'c'를 arr리스트에서 삭재한다.
del arr[2] #arr 리스트에서 2번째에 있는 값을 삭재한다.
print('a' in arr) #'a'가 arr리스트에 존재하는가? 존재하면 True 아니면 False가 출력된다.
print(len(arr)) #리스트 안에 몇개의 값이 들어있는지 출력
print(arr.count('f')) #'f'가 arr리스트에 몇개가 들어있는가
print(arr)
#숫자 리스트
num = [1,2,3,4,5]
print(sum(num)) #합 구하기
print(min(num)) #최소값
print(max(num)) #최대값

num.reverse() #역순 그로 그대로 뒤집는다.
print(num)
num.sort() # 오름차순 정렬
print(num)
num.sort(reverse=True) # 내림차순 정렬
print(num)

a = [1,2,3,4,5]
b = [2,3]
#a리스트와 b리스트를 합쳐서 출력
print(a + b)
#a리스트를 2배로 출력한다 이때 값은 모두 한 리스트안에 들어간다.
print(a * 2)
#리스트에는 요소 타입이 통합되지 않아도 됨
n = [1, "hello", 2.3]
print(n)