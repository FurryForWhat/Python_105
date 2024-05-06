fibon = [0]
my_list = [0,1]

for i in range(50):
    b = my_list[i] + my_list[i+1]
    
    if b < 50:
        fibon.append(b)
        
    my_list.append(b)
    
print(fibon)
    