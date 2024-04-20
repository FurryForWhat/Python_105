fast_food = [81,2,42,21,25,1,4,5]

fast_food.sort()
print("After Sorting:",fast_food)
fast_food.reverse()
print("After Reverse:",fast_food)

under_10 = fast_food[3:]
under_10.sort()
print('Value under 10:',under_10)

above_10_to30 =fast_food[2:4]
above_10_to30.sort()
print('Value above 10 under 30:',above_10_to30)

above_30= fast_food[:2]
above_30.sort()
print('Value abbve 30:',above_30) #index slicing