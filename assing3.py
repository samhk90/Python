print("***ASSINGMENT-03***")
print("a) To display word with the longest length")
n=int(input("Enter the no. of strings"))
l=[]
for i in range(0,n):
  z=input("Enter string:: ")
  l.append(z)
for i in l:
  for j in l:
    if len(i)>len(j):
      longest=len(i)
for k in l:
  if len(k)==longest:
    print("word with the longest length",k)
print("b) To determines the frequency of occurrence of particular character in the string")
a=input("Enter your string:: ")
r=input("Enter your chareacter:: ")
count=0
for i in a:
  for j in i:
      if j==r:
        count+=1
print(count)
print("c) To check whether given string is palindrome or not")
a1=input("Enter srting:: ")
for i in a1:
  if i==i[::-1]:
    print("string is palindrome")
  else:
    print("string is not palindrome")
  break
print("d)To display index of first appearance of the substring")
w=input("Enter the string:: ")
z=input("Enter letter:: ")
for j in w:
  if z==j:
    ind=w.index(j)+1
    print("index of first appearance of the substring",ind)
    break
print("e)To count the occurrences of each word in a given string")
count1=0
n1=int(input("Enter the no. of strings"))
l1=[]
for j in range(0,n1):
  m4=input("Enter your string:: ")
  l1.append(m4)
Frequency={}
count=0
for i in l1:
  for j in l1:
    if i==j:
      count+=1
      Frequency[i]=count
  count=0
print(Frequency)
