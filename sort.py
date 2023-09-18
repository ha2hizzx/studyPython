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
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self. grade, self.age))
    student_tuples = [
    ('John', 'A', 15),
    ('Kay', 'B', 13),
    ('Dave', 'B', 10),
]
    sorted(student_tuples, key=lambda student: student.age)
#bubble_sort
array = [4, 2, 1, 3, 5, 8, 6, 7, 9]
arr = [51, 23, 5, 1,87, 192, 72, 92]
def bubble_sort(array):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                print(array)
print("array-------")
print("before : ", array)
bubble_sort(array)
print("after : ", array)
print("arr-------")
print("before : ", arr)