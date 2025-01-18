num=int(input("Enter a number"))
flag=False

for i in range(2,num):
     if num%2==0:
          flag=True
          break
if flag:
     print(num, "is not a prime")
else:
     print(num,"is a prime")    
