#Program to calculate the length using cartesian system
import math

def calculate():
    print("Enter values for (x1,y1)")
    x1=int(input())
    y1=int(input())
    print("Enter value for (x2,y2)")
    x2=int(input())
    y2=int(input())
    length = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) * 1.0)
    return length

result = calculate()
print("The Length is ",result)