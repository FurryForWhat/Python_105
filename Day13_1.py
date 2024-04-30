num_list =[33,8,4,2,48,40] #[1,2,12,33,40,48]
copy_list = [33,8,4,2,48,40]
copy_list.sort()
copy_list.reverse()

#Procedural programming 
# Sort()
# for i in range(len(num_list)-1):
#     for j in range(len(num_list)-1-i):
#         if num_list[j] > num_list[j+1]:
#             template = num_list[j]
#             num_list[j] = num_list[j+1]
#             num_list[j+1] = template

# Reverse()
for i in range(len(num_list)-1):
    for j in range(len(num_list)-1-i):
        if num_list[j] < num_list[j+1]:
            template = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = template
            
print(num_list)
print(copy_list)