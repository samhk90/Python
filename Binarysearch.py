#BINARY SEARCH
def binsearch(l1,n):
  l=0
  h=len(l1)-1
  l1.sort()
  while l<=h:
    mid=(l+h)//2
    if l1[mid]==n:
      print("location= ",mid+1)
      return True
    else:
      if l1[mid]<n:
        l=mid+1
      else:
        h=mid-1
  return False
s1=[]
k1=int(input("Enter the no. of student:: "))
for i in range(0,k1):
  roll1=int(input("Enter Roll no.:: "))
  s1.append(roll1)
r1=int(input("Enter searching number:: "))
if binsearch(s1,r1):
  print("Found")
else:
  print("not found")
