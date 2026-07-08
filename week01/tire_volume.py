#I add the question to ask the user if they want to buy the tires and if yes, I ask for their name and phone number.
import math
from datetime import date
with open("volumes.txt", "at") as file:
    today = date.today()
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
    pi = math.pi
    volume = pi * width ** 2 * ratio * (width * ratio + 2_540 * diameter) / 10_000_000_000
    print(f"The approximate volume is {volume:.2f} liters")
    user_input = input("Would you like to buy these tires dimensions? (yes/no): ")
    if user_input.lower() == "yes":
        name = input("Please enter your name: ")
        phone = input("Please enter your phone number: ")
        file.write(f"{today}, {width}, {ratio}, {diameter}, {volume:.2f}, {name}, {phone}\n")
    else:
        file.write(f"{today}, {width}, {ratio}, {diameter}, {volume:.2f}\n")