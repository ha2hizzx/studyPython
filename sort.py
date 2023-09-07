#sorted : 순서대로 정렬
x = [1, 11, 2, 3]
y = sorted(x)
print(x)
print(y)
#reversed : 거꾸로 뒤집기
x = [1, 11, 2, 3]
y = reversed(x)
print(x)
#print(y)  :    <list_reverseiterator object at 0x1060c9fd0>
print(list(y))
num = [33, 2, 81, 21, -2, 41, 62, 23]
num.sort()
print(num)
#소문자
str1 = ['h', 'e', 'l', 'l', 'o', 'p', 'y']
str1.sort()
print(str1)
#대문자
str2 = ['h', 'e', 'l', 'l', 'o', 'p', 'y', 'H', 'E', 'L', 'L', 'O', 'P', 'Y']
str2.sort()
print(str2)
a = [3, 2, 8, 4, 1, 10, 99, 5]
b = [3, 2, 8, 4, 1, 10, 99, 5]
c = [3, 2, 8, 4, 1, 10, 99, 5]
#기본(오름차순)
a.sort()
print(a)
#오름차순
b.sort(reverse=False)
print(b)
#내림차순
c.sort(reverse=True)
print(c)
#문자열 sorted
sorted("My name is Kim Dong Hyuon". split(), key=str.lower)
student_tuples = [
    ('John', 'A', 15),
    ('Kay', 'B', 13),
    ('Dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])