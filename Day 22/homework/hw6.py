def check_voting_age(age):
    if age >= 18:
        print("თქვენ გაქვთ ხმის მიცემის უფლება")
    else:
        print("თქვენ არ გაქვთ ხმის მიცემის უფლება")

age = int(input("შემოიტანეთ თქვენი ასაკი: "))
check_voting_age(age)