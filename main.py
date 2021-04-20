with open('currenecyData.txt') as f:
    lines = f.readlines()

currency_dict = {}

for line in lines:
    parsed = line.split("\t")
    currency_dict[parsed[0]] = parsed[1]


amount = int(input("Enter the amount in INR: "))
print("Enter the name of currency to convert: ")
[print(item) for item in currency_dict.keys()]
currency = input("Please enter one of these values :")
print(f"{amount} INR is equal to {amount * float(currency_dict[currency])} {currency}")



