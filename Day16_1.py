my_data = input('Enter three values: ').split(',') #12,11,10
greatest = 0
for i in range(0,len(my_data)-1):
    if int(my_data[i]) > int(my_data[i+1]):
        greatest = my_data[i]
    else:
        greatest = my_data[i+1]
        
print('The greatest value is',greatest)