print("****ASSINGMENT-01****")
n=int(input("Enter no. of students for cricket:: "))
grpA=[]
grpB=[]
grpc=[]
for i in range(0,n):
  m=(input("Enter name of students:: "))
  grpA.append(m)
z=int(input("Enter no. of students for Badminton:: "))
for i in range(0,z):
  k=(input("Enter name of students for badminton:: "))
  grpB.append(k)
p=int(input("Enter no. of students for Football:: "))
for i in range(0,p):
  v=(input("Enter name of students for football:: "))
  grpc.append(v)
print("Student wo play cricket",grpA)
print("student who play badminton",grpB)
print("student who play football",grpc)
l1=[]
l2=[]
l3=[]
l5=[]
l4=grpA+grpc
for i in range(0,len(grpA)):
  for j in range(0,len(grpB)):
    if grpB[j]==grpA[i]:
      l1.append(grpB[j])
for i in range(0,len(grpA)):
  for j in range(0,len(grpc)):
    if grpc[j]==grpA[i]:
      l5.append(grpc[j])
l2=grpA+grpB
for i in l1:
 l2.remove(i)
l3=grpc
for i in grpc:
  for j in grpA:
    if i==j:
      l3.remove(j)
for i in grpc:
  for j in grpB:
    if i==j:
      l3.remove(j)
for k in grpA:
  for s in grpB:
    if s==k:
     l4.remove(s)
for i in l4:
  for j in grpB:
    if i==j:
      l4.remove(j)

for i in l5:
 l4.remove(i)
print("1. List of students who play both cricket and badminton:: ",l1)
print("2. List of students who play either cricket or badminton but not both:: ",l2)
print("3. Number of students who play neither cricket nor badminton:: ",l3)
print("4. Number of students who play cricket and football but not badminton:: ",l4)
