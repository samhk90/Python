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
l4=[]
l1=[]
l5=[]
l6=[]
for i in range(0,len(grpA)):
  for j in range(0,len(grpB)):
    if grpB[j]==grpA[i]:
      l1.append(grpB[j])
l4=grpA+grpB
l7=grpA+grpc
l5=list(set(l4)-set(l1))
l6=list(set(grpc)-set(l4))
l8=list(set(l7)-set(grpB))
print("1. List of students who play both cricket and badminton:: ",l1)
print("2. List of students who play either cricket or badminton but not both:: ",l5)
print("3. Number of students who play neither cricket nor badminton:: ",l6)
print("4. Number of students who play cricket and football but not badminton:: ",l8)
