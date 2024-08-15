def calculate_rectangle_area(length, width):
    area = length * width
    return area

def calculate_rectangle_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("მართკუთხედის სიგრძე: "))
width = float(input("მართკუთხედის სიმაღლე: "))

area = calculate_rectangle_area(length, width)
perimeter = calculate_rectangle_perimeter(length, width)

print("მართკუთხედის ფართობი:", area)
print("მართკუთხედის პერიმეტრი:", perimeter)