print("***ASSINGMENT-02***")
print("Enter Ab for absent student")
n=int(input("Enter no. of students:: "))
marks={}
m3={}
m2={}
m4=[]
sum=0
count=0
for i in range(0,n):
  z=input("enter name of student:: ")
  m=((input("Enter mraks:: ")))
  marks.update({z:m}) 
  if m=="Ab":
    m2.update({z:m})
  else:
    v=int(m)
    m3.update({z:v}) 
    m4.append(v)
if m3=={}:
  print("whole class was absent")
else:
 for j in m3.values(): #for counting of absen student
   sum=sum+j
for i in marks.values():
   if i=="Ab":
     count=count+1
k=n-count 
avg=sum/k #avg calculation
max=0
for i in m3.values(): #for max values
  if i>max:
    max=i
for j in m3.values(): #for minimum values
  for i in m3.values():
   if j<i:
     min=j
     break
   if i<j:
    min=i 
    break
print("1.Avg score of class:: ",avg)
for i in m3:
  if m3[i]==max:
    print("2.Highest marks in class:: ",max,"got by",i)
  if m3[i]==min:
    print("2.Lowest marks in class:: ",min,"got by",i)
print("3.Number of students who was absent:: ",count)
m4=list(m3.values())
Frequency={}
count=0
for i in m4:
  for j in m4:
    if i==j:
      count+=1
      Frequency[i]=count
  count=0
high=0
print(Frequency)
for i in Frequency.values(): #for max values
  if i>high:
    high=i
for i in Frequency:
  if Frequency[i]==high:
    print("4.Highest Frequency is",i,"and frequency is",Frequency[i])
