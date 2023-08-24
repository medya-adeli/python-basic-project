customer = []
index=0
max_value = 0

while len(customer) <= 10:
    customer.append(int(input("Enter for the first customer: ")))
    print(customer)
    if customer[index]>max_value:
        max_value = customer[index]
    index+=1
    print("max sales :",max_value)


