
number = int(input("Enter a number: "))

while number <= 0:
    print("Please enter a positive integer.")
    number = int(input("Enter a number: "))

print("Counting down from", number, "to 1:")
while number >= 1:
    print(number)
    number -= 1
