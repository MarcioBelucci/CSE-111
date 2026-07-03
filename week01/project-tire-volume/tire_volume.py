import math
from datetime import date
with open("project-t/volumes.txt", "a") as file:
    today = str(date.today())
    width = float(input("Enter the width of the tire in mm (ex 205): "))
    ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
    pi = math.pi
    volume = pi * width ** 2 * ratio * (width * ratio + 2_540 * diameter) / 10_000_000_000
    print(f"The approximate volume is {volume:.2f} liters")
    file.write(str(today))
    file.write(str(width))
    file.write(str(ratio))
    file.write(str(diameter))
    file.write(str(volume))