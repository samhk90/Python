print("***ASSINGMENT-02***")
print("Enter 0 for absent student")
n=int(input("Enter no. of students "))
marks=[]
sum=0
count=0
for i in range(0,n):
  m=int(input("Enter mraks"))
  marks.append(m)
for i in range(0,n):
  sum=sum+marks[i]
avg=sum/n
print("1.Avg score of class:: ",avg)
print("Highest marks in class:: ",max(marks))
print("Lowest marks in class:: ",min(marks))
for i in marks:
  if i==0:
    count=count+1
    break
print("Number of students who was absent:: ",count)
for i in range(0, len(marks)):
 for j in range(i+1, len(marks)):
  if(marks[i] == marks[j]):
   print("Mark with highest frequency",marks[j])