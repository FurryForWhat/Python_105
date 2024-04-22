num_list =[1,2,3] #total index 3

for num in range(len(num_list)): # 0 , 1 
    if num_list[num] > num_list[num+1]:
        num_list[num+1] = num_list[num]
        larger_number = num_list[num]
    else:
        larger_number = num_list[num+1]
