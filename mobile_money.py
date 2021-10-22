#user

print("1. send money ")
print("2. Withdraw money ")

phone_num = (int(input("Enter your phone number here: ")))
#if phone_num > or < to 10 digits:
user = input("select an option:\n ")
if user =='1':
    print("send money ")
    print("1. MTN user ")
    print("2. Airtel user ")

    x = input("choice:\n")
    if x =='1':
        print("MTN user: ")
        num = print("Enter you MTN phone number here ")
        if num == phone_num:
            amount = input("Enter the amount you want to send ")
            print(amount, "successfully sent to" phone_num)
    else:
        print("Wrong number or invalid details")
        exit()
elif x == '2':
    print("Airtel user ")
    num = print("Enter you MTN phone number here ")
    if num == phone_num:
           amount = input("Enter the amount you want to send ")
          print(amount, "successfully sent to" phone_num)
    print("Wrong number or invalid details")
    exit()
else:
    print("invalid choice, enter a valid choice")


