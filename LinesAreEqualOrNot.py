#Program to check wheather the lines are equal are not
import math


print("Enter Co-ordinates for A(x1,y1)")
x1=int(input())
y1=int(input())
print("Enter Co-ordinates for B(x2,y2)")
x2=int(input())
y2=int(input())
print("Enter Co-ordinates for C(x3,y3)")
x3 = int(input())
y3 = int(input())
print("Enter Co-ordinates for B(x4,y4)")
x4 = int(input())
y4 = int(input())
length1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
length2 = math.sqrt(math.pow(x3 - x4, 2) + math.pow(y4 - y3, 2) * 1.0)

if length2==length1:
    print("Both lines are equal")
else:
    print("lines are not equal")