int_list = [1,3,2,3,4,5]
int_list.append('Hi')
print('After adding \'Hi\' in list :',int_list)
int_list.remove('Hi')
print('After removing \'Hi\' from list :',int_list)
del int_list[4]
print('After removing 5 from list :',int_list)
print(int_list.count(3))
copy_intList = int_list.copy()
print('After copying :',copy_intList) 
copy_intList.extend(int_list)
print("After Extend:",copy_intList)
int_list.insert(1,10)
print(int_list)

