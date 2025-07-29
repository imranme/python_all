name = 'rr'
phone = '4234325435'
size_name = len(name)
size_phone = len(phone)

if(name=='' or phone==''):
    print("The name field can not be empty")
else:
    #Nested conditional statment 
    if(size_name<3):
        print("The name length must be minimam 3")
    elif(size_phone!=11):
        print("The phome number must be 11 digit")

    else:
        print('success')