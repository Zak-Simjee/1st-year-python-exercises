n=int(input())
i=0
li=[]
while i!=n:
    a=int(input())
    li.append(a)
    i=i+1
list.sort(li)
list.reverse(li)
for b in range(len(li)):
    print(li[b])

