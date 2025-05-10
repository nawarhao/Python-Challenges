#operator presedences - It is very similar to pemdas, using expressions
x = 4
y = 2
z = 9
a = 2
answer = (a+x)*z/y
print(answer)

n1 = int(input("Enter a value for the numerator: "))
n2 = int(input("Enter a value for the denominator: "))
if n1%n2==0:
    print(f"{n1} is divisible by {n2}")
else :
    print(f"{n1} is not divisble by {n2}")
    
#finding the correct mean
mean = 38
wrongnumber = 36
correctnumber = 56
totalnumber = 40

sum = mean*totalnumber
print("The sum of 40 numbers is", sum)
sum2 = sum-wrongnumber+correctnumber
print("The corrected sum is", sum2)
#the corrected mean is 
mean2 = sum2/totalnumber
print("The corrected mean is", mean2)

#finding the average speed of the three cyclists
c1 = int(input("Enter first cyclist speed: "))
c2 = int(input("Enter second cyclist speed: "))
c3 = int(input("Enter third cyclist speed: "))

average = (c1+c1+c3)/3
print("The average speed of the 3 cyclist is", average)

if c1<average:
    print("Speed 1 is lower than average with the difference of", average-c1)
if c2<average:
    print("Speed 2 is lower than average with the difference of", average-c2)
if c3<average:
    print("Speed 3 is lower than average with the difference of", average-c3)
    
#Take input values from user
x = input("Enter value of x: ")
y = input("Enter value for y: ")

#Swapping
a = x
x = y
y = a

#Display swapping results
print("value of x after swapping", x)
print("value of y after swapping", y)