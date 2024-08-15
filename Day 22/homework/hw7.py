def check_number(num):
    if num > 0:
        print("რიცხვი დადებითია")
    elif num < 0:
        print("რიცხვი უარყოფითია")
    else:
        print("რიცხვი ნულია")

num = float(input("შემოიტანეთ რიცხვი: "))
check_number(num)

