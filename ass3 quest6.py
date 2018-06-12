list=[1,2,3,]
print(list)

list.append(4)
print(list)

list.append(5)
print(list)

list.pop()
print( "stack pop implemetation ",list)


from collections import deque
list=deque([1,2,3])
print(list)

list.append(4)
print(list)

list.popleft()
print("element is pop from left most",list)

