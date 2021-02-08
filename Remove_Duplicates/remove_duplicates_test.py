#!/usr/bin/python3

import numpy as np

print(' \n REMOVE DUPLICATES \n ')

def remove_dup_in_dict(dct):
  lst = []
  lst = list(dct)
  return lst
  
def remove_dup_in_list(lst):
  lst.sort()
  i = len(lst) - 1
  while i > 0:
    if lst[i] == lst[i-1]:
      lst.pop(i)
    i -= 1
  
  return lst
  
def remove_dup_in_array(arr):
  lst = arr.tolist()
  new_list = []
  for i in lst:
    if i not in new_list:
      new_list.append(i)
  
  return new_list


m_dct = {1,1,1,2,3,3,4}
m_lst = [1,1,1,2,3,3,4]
m_arr = np.array([1,1,1,2,3,3,4])

print(' Original Item   : ', m_lst)

print(' Dictionary case : ', remove_dup_in_dict(m_dct))
print(' List case       : ', remove_dup_in_list(m_lst))
print(' Ndarray case    : ', remove_dup_in_array(m_arr))

