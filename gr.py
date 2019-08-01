x11=list(map(int,input().split()))
l=list(map(int,input().split()))
a=[]
n=x11[0]
k=x11[1]
for o in range(0,n-1):
	c=1
	for u in range(o+1,n):
		if l[o]==l[u]:
			c+=1
			t=l[u]
	if c==k:
		a.append(t)
print(*a)
