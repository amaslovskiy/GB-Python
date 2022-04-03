# password = input("Input password >>> ")
#
# original_password = "correct"
#
# if original_password == password:
#     print("password match")
# else:
#     print("not correct")


age = int(input("Tel me your age >>> "))

if age >= 14:
    print("You can get your passport")

    if 20 <= age < 45:
        print("You can exchange your passport")
    elif age < 1:
        print("Custom")
else:
    print("You didn't reach the required age")
