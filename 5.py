List1=[1,2,5,6,8,10,12]
List2=[]

for x in range(1,16):
    if x not in List1:
        List2.append(x)
print(List2)
