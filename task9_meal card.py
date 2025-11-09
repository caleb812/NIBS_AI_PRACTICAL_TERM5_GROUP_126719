# Prompt for student details
print("🌟 Welcome to the Student Meal Card System! 🌟")
print("-" * 50)
student_name = input("Enter student name: ")
adm_No = int(input("Enter admission number: "))
meal_type = input("Enter meal type (Breakfast, Lunch, Supper): ").capitalize()
amountpaid = {"Breakfast": 100, "Lunch": 200, "Supper": 250}
mealcard = 1000

if meal_type not in amountpaid:
    print("Invalid meal type. Please enter Breakfast, Lunch, or Supper.")
else:
    cost = amountpaid[meal_type]
    advice = "Maintain weekly top-up schedule"
    remaining_balance = mealcard - cost

    # Balance status
    if remaining_balance < 150:
        print("Low balance.")
    else:
        print("Sufficient amount.")
        
print("="*50)
    # Output 
print(f"Student Name: {student_name}")
print(f"Admission Number: {adm_No}")
print(f"Meal Type: {meal_type}")
print(f"Cost: {cost} KES")
print(f"Remaining Balance: {remaining_balance} KES")
print(f"Advice: {advice}")