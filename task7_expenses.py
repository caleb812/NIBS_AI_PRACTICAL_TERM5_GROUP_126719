#input expenses
food= int(input("Enter food🍛 expenses: "))
transport=int( input("Enter transport🚕 expenses: "))
utilities=int( input("Enter utilities expenses: "))

total= food+transport+utilities
percentage_of_food=(food/total)*100
percentage_of_transport=(transport/total)*100
percentage_of_utilities=(utilities/total)*100

print(f"Food: {percentage_of_food:.1f}%")
print(f"Transport: {percentage_of_transport:.1f}%")
print(f"Utilities: {percentage_of_utilities:.1f}%")

if food > 50:
    print("You are overspending on food.")
else:
    print("Minimize the expenses.")
if utilities < 20:
    print("utilities spending is minimal.")
else:
    print("Utilities spending is significant.") 
    # Display neat table
    print("\n" + "="*50)
    print(f"{'EXPENSE BREAKDOWN':^50}")
    print("="*50)
    print(f"{'Category':<15} {'Amount ($)':<15} {'Percentage (%)':<15}")
    print("-"*50)
    print(f"{'Food':<15} {food:<15.2f} {percentage_of_food:<15.1f}")
    print(f"{'Transport':<15} {transport:<15.2f} {percentage_of_transport:<15.1f}")
    print(f"{'Utilities':<15} {utilities:<15.2f} {percentage_of_utilities:<15.1f}")
    print("-"*50)
    print(f"{'TOTAL':<15} {total:<15.2f} {100.0:<15.1f}")
    print("="*50)