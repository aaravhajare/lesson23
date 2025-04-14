
n1 = [1,2,3]
n2 = [4,5,6]

result = map(lambda x,y : x * y , n1 ,n2)
print(list(result))


num = [1,2,3,4,5,6]

def square(n):
    return n*n

result = list(map(square,num))

print(result)