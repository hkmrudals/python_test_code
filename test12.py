# def add():
#     a = int(input('숫자>>>'))
#     b = int(input('숫자 >>>'))
#     print(a+b)

# add()

# def add(a,b):
#     print(a+b)
    
# a = int(input('숫자>>>'))
# b = int(input('숫자 >>>'))
# # add(a,b)
# add(b=a,a=8)

# def add(*a):
#     print(a)
#     print(type(a))
#     result = 0    
#     for i in a:
#         result += i
#     return result
# print(add(1,3,5,7,0))
# print(add(2,4,6,8,9))

# def add(*a, choice = 'sub'):
#     print(a)
#     print(type(a))
#     print(choice)
#     result = 0    
#     for i in a:
#         result += i
#     return result
# print(add(1,3,5,7,0, choice='add'))
# print(add(2,4,6,8,9))

# def print_kwargs(**a):
#     print(a)
#     print(type(a))
    
# print_kwargs(Name='hong', age=22, city='busan')

# def add_and_mul(a,b):
# return a+b, a*b

a = 1
def vartest(a):
    a = a + 1
    print('함수안', a)
    return a

a = vartest(a)
print(a)

