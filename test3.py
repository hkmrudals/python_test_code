jumin = "098765-1234567"

print("성별 : ", jumin[7])
print("연 : ", jumin[0:2])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[-7:])


python = "python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java"))
print("hi")
print(python.count("n"))