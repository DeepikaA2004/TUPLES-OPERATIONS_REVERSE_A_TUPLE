'''def rev(t):
 res = t[::-1]
 return res'''
def rev(t):
 res = ()
 for k in reversed(t):
  res = res + (k,)
 return res
n=int(input("Enter number of elements in tuple "))
l=list()
for i in range(0,n):
 e=input("Enter the value: ")
 l.append(e)
a=tuple(l)
print(rev(a))