name=input("Enter Name:")
mark1=int(input("Enter 1st mark :"))
mark2=int(input("Enter 2nd mark :"))
mark3=int(input("Enter 3rd mark :"))
average=(mark1+mark2+mark3)/3
print("-"*50)
if average >= 80 and average <= 100:
    grade='A'
    comment='Excellent'
elif average >=70:
    grade='B'
    comment='very Good'
elif average >=60:
    grade='C'
    comment='Good' 
elif average >=50:
    grade='D'
    comment='improve' 
else:
    grade='F'
    comment='Fail' 
#output
print("="*50)
print("Your Name is:",name)
print(f"mark1:{mark1}")                  
print(f"mark2:{mark2}")
print(f"mark3:{mark3}")
print(f"mark1:{mark1}")
print(f"Average:{average}")
print(f"Your Grade is:{grade}")
print(f"comment:{comment}")    