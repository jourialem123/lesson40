#Write a Python program for printing the sum of the first ten natural numbers using the while loop.
i=1
sum1=0
while i<11:
    sum1=sum1+i
    i=i+1
print("The sum of 11 natural numbers is ",sum1)

totalsum=sum(range(1,11))
print("The sum of 11 natural numbers is ",totalsum)
