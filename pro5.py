def f(s,n,m):
	su=0
	while(True):
		su+=n+m
		if s==su:
			return 'yes'
		if su>s:
			break
	return 'no'
def main():
	n=int(input())
	a=int(input())
	b=int(input())
	print(f(n//2,a,b))
  
try:
  main()
except:
  print('invalid')
