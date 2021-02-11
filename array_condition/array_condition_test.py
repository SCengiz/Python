'''
  How do we compute the indices for an array in Python, at which a certain
    condition is satisfied
'''
import numpy as np

def first_test(condition, arr):

  print('\n *** FIRST TEST *** ')
  
  #true_indexes is a tuple we need we take its first arg.
  true_indexes = np.where(condition)
  print(' True indexes in array :  ', true_indexes[0])
  
  def return_values():

    true_values = np.array([])
    kk = 0
    for i in true_indexes[0]:
      true_values = np.append(true_values, arr[i])
      kk += 1
    return true_values

  print(' True values in array   :  ',  return_values())


def second_test(arr):
  
  print('\n *** SECOND TEST *** ')
  
  #This gives us a list type.
  true_indexes \
    = [index for index,value in enumerate(arr) if value > 2]

  #Cast to ndarray.
  true_indexes = np.array(true_indexes)
  
  print(' True indexes in array :  ', true_indexes)
  
  #print(arr[i], " ", end = '')
  
  fh_print = lambda true_indexes : [ arr[i] for i in true_indexes ]  
  
  print(' True values in array   :   ', end = '')
  print(fh_print(true_indexes))
  
  
def third_test(arr):
  
  print('\n *** THIRD TEST *** ')
  
  true_indexes \
    = [index for index in range(len(arr)) if arr[index] > 2]

  #Cast to ndarray.
  true_indexes = np.array(true_indexes)
  
  print(' True indexes in array :  ', true_indexes)
  
  print(' True values in array   :  [', end = '')
  
  for i in true_indexes:
    print(arr[i], " ", end = '')
  
  print(']')


if __name__ == "__main__":

  i_array = np.array([i for i in range(-5,6)]);

  #This is my condition for founding this items in array  
  my_condition = i_array > 2

  first_test(my_condition, i_array)
  second_test(i_array)
  third_test(i_array)

