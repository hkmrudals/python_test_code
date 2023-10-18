result1 = 0
result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add2(4))
# print(add1(3))
# print(add2(4))

# class Calculator:                   # 계산기
#     count = 0
#     def __init__(self):
#         Calculator.count += 1
#         self.count = Calculator.count
#         self.result = 0
        
#     def add(self,num):
#         self.result += num
#         return self.result
    
#     def sub(self,num):
#         self.result -= num
#         return self.result

# print(Calculator.count)

# a = Calculator()
# # print(Calculator.count)
# print(a.count)

# b = Calculator()
# print(Calculator.count)
# print(a.count)
# print(b.count)

# print(a.add(4))
# print(a.add(5))

# print(b.add(6))
# print(b.add(7))

# print(a.sub(8))

# class Test:
#     count = 0 # 클래스 변수 선언
#     def __init__(self, name = '아무개', age = 0):
#         self.name = name
#         self.age = age
#         Test.count += 1
#         self.count = Test.count

#     def __str__(self):
#         return f'Test class [{self.count}번, {self.name}, {self.age}]'

# t1 = Test('홍홍홍', 23)
# t2 = Test('김김김')
# t3 = Test()

# print(t1)
# print(t2)
# print(t3)

class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender
    def about_me(self):
        print(f"저의 이름은 {self.name}이고, 나이는 {self.age}살, 성별은 {self.gender}성입니다.")
      
class Animal:
    def talk(self):
        print('talk')

class Employee(Person, Animal):
    def __init__(self, name, age, gender, job, salary, hire_date) -> None:
        super().__init__(name, age, gender)
        self.job = job
        self.salary = salary
        self.hire_date = hire_date
    def about_me(self):
        super().about_me()
        print(f'{self.job}직이고, 연봉은 {self.salary}만원, 입사일자는 {self.hire_date}입니다.')
    
a1 = Employee('이이이', 22, '남', '영업', 3200, '2023-01-01')
a1.about_me()
a2 = Person('안안안', 33, '여')
a2.about_me()