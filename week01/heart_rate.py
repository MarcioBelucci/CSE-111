"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.

Ask for a person’s age and computes and outputs the slowest and fastest rates necessary to strengthen his heart.
"""

age = int(input("How old are you? "))
maximum_rate = 220 - age
fastest_rate = maximum_rate * 0.85
slowest_rate = maximum_rate * 0.65

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {slowest_rate:.0f} and {fastest_rate:.0f} beats per minute. ")

