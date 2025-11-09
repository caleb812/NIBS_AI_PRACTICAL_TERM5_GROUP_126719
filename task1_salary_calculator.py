#TASK 1.
# (a) Input employee details
payrollnumber = input("Enter payroll number: ")
name = input("Enter name: ")
gender = input("Enter gender: ")
jobgroup = input("Enter job group (j, k, l, m): ").lower()  
basicsalary = float(input("Enter basic salary: "))
       

# Allowances dictionary
allowances_dict = {
    'j': 5000,
    'k': 5500,
    'l': 6000,
    'm': 6500,
}

# Validate job group
if jobgroup not in allowances_dict:
    print("Invalid job group! Please enter j, k, l, or m.")
    exit()

# Get allowance amount based on job group
allowance = allowances_dict[jobgroup]

# (b) Computing
grosspay = basicsalary + allowance
taxes = 0.12 * basicsalary  # 12% tax
netpay = grosspay - taxes

# (c) Display 
print("\n" + "="*40)
print("EMPLOYEE PAYROLL DETAILS")
print("="*40)
print(f"Payroll Number: {payrollnumber}")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Job Group: {jobgroup.upper()}")
print(f"Basic Salary: Ksh {basicsalary:,.2f}")
print(f"Allowance: Ksh {allowance:,.2f}")
print(f"Gross Pay: Ksh {grosspay:,.2f}")
print(f"Taxes (12%): Ksh {taxes:,.2f}")
print(f"Net Pay: Ksh {netpay:,.2f}")
print("="*40)