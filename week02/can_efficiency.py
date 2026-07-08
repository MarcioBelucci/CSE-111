import math
def main():
    name = input("Enter the name: ")
    radius = float(input("Enter the radius:"))
    height = float(input("Enter the height:"))
    can_eff(name, radius, height)

def can_eff(name, radius, height):
    volume = can_vol(radius, height)
    area = can_area(radius, height)
    eff = volume / area
    print(f"{name} volume={volume:.2f}, area={area:.2f}, efficiancy{eff:.2f}")

def can_vol(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume

def can_area(radius, height):
    area = 2 * math.pi * radius * (radius + height)
    return area
main()