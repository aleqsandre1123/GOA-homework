def check_age_category(age):
    if age < 13:
        print("ბავშვი ხარ")
    elif age >= 13 and age <= 19:
        print("შენ ხარ მოზარდი")
    else:
        print("სრულწლოვანი ხარ")

age = int(input("შემოიტანეთ თქვენი ასაკი: "))
check_age_category(age)