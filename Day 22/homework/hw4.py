def calculate_rectangle_perimeter(side1, side2, side3, side4):
    perimeter = side1 + side2 + side3 + side4
    return perimeter

side1 = float(input("მეარჯვენა გვერდი: "))
side2 = float(input("მექვე გვერდი: "))
side3 = float(input("მესამე გვერდი: "))
side4 = float(input("მეოთხე გვერდი: "))

perimeter = calculate_rectangle_perimeter(side1, side2, side3, side4)

print("მართკუთხედის პერიმეტრი:", perimeter)

