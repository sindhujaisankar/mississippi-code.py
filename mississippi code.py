str1=input("enter the string: ")
d1=dict()
for i in str1:
    if i in d1:
        d1[i]=d1[i]+1
    else:
        d1[i]=1
print(d1)
