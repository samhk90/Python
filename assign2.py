print("***ASSINGMENT-02***")
print("Enter Ab for absent student")
n=int(input("Enter no. of students:: "))
marks={}
m3={}
m2={}
sum=0
count=0
for i in range(0,n):
  z=input("enter name of student")
  m=((input("Enter mraks:: ")))
  marks.update({z:m}) 
  if m=="Ab":
    m2.update({z:m})
  else:
    v=int(m)
    m3.update({z:v}) 
if m3==[]:
  print("whole class was absent")
else:
 for j in m3.values():
   sum=sum+j
for i in marks.values():
   if i=="Ab":
     count=count+1
k=n-count
avg=sum/k
print("1.Avg score of class:: ",avg)
print("2.Highest marks in class:: ",max(m3.values()))
print("2.Lowest marks in class:: ",min(m3.values()))
print("3.Number of students who was absent:: ",count)

for i in m3.values():
 for j in m3.values():
  if(i==j):
   print("4.Mark with highest frequency:: ",j)
   break
  break
