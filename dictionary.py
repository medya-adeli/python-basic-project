i=dict()
while True:
    a=int(input("enter number:"))
    if a==1:
        search=input("enter for search:")
        if search in i:
            print("mojod ast")
            print(i)
        else:
            print(i)
    elif a==2:
        add_1=input("enter words in english:")
        add_2=input("enter words in kurdish:")
        if add_1.lower() in i and i[add_1] == add_2:
            print("Words are already in the dictionary.")
        else:
            i.update({add_1:add_2})
            print("Dictionary updated:", i)
    elif a==3:
        print("Current dictionary:", i)
    elif a==4:
        exit()