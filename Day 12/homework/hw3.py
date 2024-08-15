
num = int(input("Enter a positive integer: "))

while num <= 0:
    print("Please enter a positive integer.")
    num = int(input("Enter a positive integer: "))

sum_of_numbers = 0
for i in range(1, num + 1):
    sum_of_numbers += i

print("The sum of all numbers from 1 to", num, "is:", sum_of_numbers)
