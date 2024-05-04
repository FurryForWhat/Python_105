my_string = '123456789089'
data_flag = True
for i in range(len(my_string)):
    for j in range(i+1,len(my_string)):
        if my_string[i] == my_string[j]:
            print('Same data found:',my_string[i])
            data_flag = False

if data_flag:
    print("Same data not found")