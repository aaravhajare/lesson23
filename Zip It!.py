s1 = {1,3,2}
s2 = {"b","a","c"}

s3 = list(zip(s1,s2))
print(s3)

list1 = [1,2,3,4]
list2 = [100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

playrs  = ["a" , "b" , "c"]
languages = ["python" , "java" , "c++"]

dict1 = dict(zip(playrs,languages))
print(dict1)