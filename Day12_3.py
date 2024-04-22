num_list = [12,34,5,19,200,21]
larger_number = 0
for num in range(len(num_list)-1):
    if num_list[num] > num_list[num+1]:
        num_list[num+1] = num_list[num]
        larger_number = num_list[num]
    else:
        larger_number = num_list[num+1]

print('The largest number is',larger_number)
