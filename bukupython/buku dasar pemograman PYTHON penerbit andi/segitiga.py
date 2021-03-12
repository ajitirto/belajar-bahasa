######membuat segita bisa
##def jumlahderet(x):
##  b=0
##  for i in range(x+1):
##    a=i
##    b=b+a
##  print b


print "Sign up:"
k=raw_input("Enter your name:")
n=raw_input("Enter your nim:")
m=raw_input("enter your email")

print '''
  success

----------------------'''
print "login"
print "username     :",m
while 2==2:
  p=raw_input("password     :")
  pas = k[0] + n[-3:]
  if p==pas:
    print '''login succes!
 Welcome to %s's account'''%(k)
    break
  else :
    print 'password is wrong'
