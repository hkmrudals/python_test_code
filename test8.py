cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get[5])
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())
