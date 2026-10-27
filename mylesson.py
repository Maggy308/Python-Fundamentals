#True Fals

print(10>5)
print(10==10.0)
print(32>=34)
print(10!=10)
print(10!=1)

score=int(input("Please Enter your score:"))
if score >=90:
    print('A')
elif 80 <= score < 90:
    print("A-")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("C")
elif 50 <= score <= 59:
    print("D")
else:
    print("FAIL")