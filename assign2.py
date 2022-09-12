print("***ASSINGMENT-02***")
print("Enter Ab for absent student")
n=int(input("Enter no. of students:: "))
marks=[]
m3=[]
m2=[]
sum=0
count=0
for i in range(0,n):
  m=(input("Enter mraks:: "))
  marks.append(m)  
  if m=="Ab":
    m2.append(m)
  else:
    z=int(m)
    m3.append(z)
if m3==[]:
  print("whole class was absent")
else:
 for j in range(0,len(m3)):
   sum=sum+m3[j]
 avg=sum/n
 print("1.Avg score of class:: ",avg)
 print("2.Highest marks in class:: ",max(m3))
 print("2.Lowest marks in class:: ",min(m3))
 for i in range(0, len(m3)):
  for j in range(i+1, len(m3)):
   if(m3[i] == m3[j]):
    print("4.Mark with highest frequency:: ",marks[j])
    break
for i in marks:
   if i=="Ab":
     count=count+1
print("3.Number of students who was absent:: ",count)
