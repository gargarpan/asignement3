
even=0
odd=0
list=[1,2,3,4,5,6]
print(list)
for n in list:
    if n%2==0:
        even=even+1
    else:
        odd=odd+1

print("even count  ",even)
print("odd count",odd)
