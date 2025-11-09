import math
a= float(input("Enter a:"))
b= float(input("Enter b:"))
c= float(input("Enter c:"))
part= (b**2) - (4*a*c)
if part > 0:
    root1= (-b + math.sqrt(part))/(2*a)
    root2= (-b - math.sqrt(part))/(2*a) 
    print(f"Roots are real and distinct:{root1} and {root2}") 
elif part == 0:
    root =-b/(2*a)
    print(f"roots are real and equal {root}")
else:
    root=-b/(2*a)
    root3=math.sqrt(-part)/(2*a) 
    print(f"roots are complex: {root}+ {root3} and {root} - {root3} ")
    