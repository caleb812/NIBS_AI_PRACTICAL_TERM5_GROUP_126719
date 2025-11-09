#temperature advisor
temperature=float(input("Enter temperature: ")) 
if temperature < 15:
    print("It's cold- wear a jacket. ")
elif temperature >= 15 and temperature <=25:
    print("The weather is pleasant- enjoy your day. ")
elif temperature > 25:
    print("It's hot- stay hydrated. ")
else:
    print("Please enter a valid number for temperature.")
    