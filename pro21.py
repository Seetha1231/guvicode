def  main():
	s=0
	l=[]
	n=int(input())
	for i in range(n):
		l.append(int(input()))
	sub=n//2
	for i in range(sub):
		s+=l[i]
	sub1=s/sub
	s=0
  for i in range(n-sub,n):
		s+=l[i]
	sub2=s/sub
  print(l)
	if sub1==sub2 :
		if l[sub]==sub1 :
			print('yes')
		else :
			print('no')
      
try:
  main()
except:
  print('invalid')
