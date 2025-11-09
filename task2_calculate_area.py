#user input
import math
a =float( input("Enter A: "))
b = float(input("Enter B: "))
h = float(input("Enter H: "))
area_of_trapezium=(1*(a+b)*h)/2
r=float(input("Enter Radius:"))
area_of_circle=math.pi * r**2
area_of_shaded_region=area_of_trapezium-area_of_circle
#output
print("area_of_trapezium:",area_of_trapezium)
print("area_of_circle:",area_of_circle)
print("area_of_shaded_region:",area_of_shaded_region)