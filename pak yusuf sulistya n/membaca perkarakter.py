##Read to character 
Vocal="AIUEOaiueo"
Consonant="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
Number="1234567890"
Character="!@#$%^&*()"
Point="."
Space=" "
Line="\n"
Avocal=0;
Aconsonant=0;
Anumber=0;
Acharacter=0;
Amark=0;
Apoint=0;
Aspace=0;
Aline=0;
Aother=0;

o=open('C:\Users\HP\Desktop\Historypython.txt','r')

while 1==1:
  s= o.readline()
  if "readline()" in s[-1:]:
    a=s[0:-1]
  else:
    a=s
  for i in a:
    if i in Vocal:
      Avocal=1+Avocal
    elif i in Consonant:
      Aconsonant=1+Aconsonant
    elif i in Number:
      Anumber=1+Anumber
    elif i in Point:
      Apoint= 1+Apoint
    elif i in Space:
      Aspace = 1+Aspace
    elif i in Line:
      Aline = 1+ Aline
    elif i in Character:
      Acharacter = 1+Acharacter
    elif i in Point:
      Apoint = 1+Apoint
    elif i in Space:
      Aspace = 1+Aspace
    else:
      Aother = 1+Aother
  if s== "":
    break
    
