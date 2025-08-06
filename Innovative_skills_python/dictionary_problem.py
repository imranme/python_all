product= {
    'naem':['p1', 'p2','p3','p4'],
    'price': [100, 200, 300, 400]
}

key_list = list(product) 

for i in range(len(product[key_list[0]])):
    for j in range(len(key_list)):
        colum = key_list[j] 
        print(product[colum][i], end= ' ')

    print()