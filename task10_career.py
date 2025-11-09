# Prompt student details
print("🎓 Welcome to the Career Guidance System! 🎓")
print("-"*40)
student_name = input("Enter student name: ")
subject = input("Enter subject (Math, Science, Business, Art, Home Science): ").strip().title()

if subject == 'Math':
    career = "Data Analyst / Engineer"
elif subject == 'Science':
    career = "Lab Technician / Researcher"
elif subject == 'Art':
    career = "Designer / Animator"
elif subject == 'Business':
    career = "Marketer / Accountant"
elif subject == 'Home Science':
    career = "Catering & Accommodation"
else:
    career = "Invalid subject. Please choose a valid option."

# Output
print("="*40)
print(f"Student Name : {student_name}")
print(f"Subject      : {subject}")
print(f"Career Path  : {career}")
