#TASK 4.
customername =str( input("Enter customer name: "))
age =int( input("Enter age: "))
monthlyincome = int(input("Enter monthly income: "))
creditscore =int( input("Enter credit score: "))
if monthlyincome >= 30000 and creditscore >= 700:
    print("Approved")
    print("He or she has met the requirement")
else:
    print("Rejected")