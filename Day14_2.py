data_list = ['p','q']
num = int(input('Enter number: '))
template = []
for_p = data_list[0]
for_q = data_list[1]
for i in range(1,num+1):
    new_dataOne = for_q+str(i)
    new_dataTwo = for_p+str(i)  
    template.append(new_dataOne)
    template.append(new_dataTwo)

print('Data is',template)