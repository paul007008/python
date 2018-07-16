#!/usr/bin/python
 
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
 
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:7:2])
print("list2[1:5]: ", list2[1:])
print("list2[1:5]: ", list2[-1])
print("list2 is len:",len(list2))
if(3 in list2):
    print("OK")