vehicle_name=(input("Enter vehicle name: "))
speed= int(input("Enter speed(km/h): "))
if speed <=80 :
    print(" No fine")
elif speed >= 81 and speed <=100:
    print(" fine = 3000")
elif speed >= 101 and speed <120:
    print(" fine = 7000")
else:
    print(" fine = 15000")
    #output
    print(f"Vehicle: ",vehicle_name)
print(f"Speed: {speed} km/h")
    