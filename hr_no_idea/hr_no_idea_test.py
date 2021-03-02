"""
 Solution for "https://www.hackerrank.com/challenges/no-idea/problem"

"""
import numpy as np
import sys

# Call this function when input arguments entered wrongly
def usage():
  print("\n *** USAGE *** \n")
  print(" Input array length must be -> n ")
  print(" Sets length must be -> m \n")

# Find duplications in array if any duplicated is happen then flag will be true.
# Get rid of duplicates in array.
def check_remove_dup_in_array(in_array):
  remove_arr = np.empty(0, dtype = int)
  duplicate_flag = False
  for item in in_array:
    if item not in remove_arr:
      remove_arr = np.append(remove_arr, item)
    else:
      duplicate_flag = True
      
  return duplicate_flag, remove_arr

# Create sets A and B with obeying the rulese.
# The rules are firstly length must ben equals exatly m and
# ... Sets will not contain duplicated items
def create_sets(in_m):
  set_list = []
  set_list = [ int(kk) for kk in input(" set array : ").split() ]    
  set_array = np.asarray(set_list)
  
  if len(set_list) != in_m or check_remove_dup_in_array(set_array)[0]:
    print(" Much or less input arguments for set or duplicated items detected !!! ")
    usage()
    sys.exit(-1)
  else:
    
  return set_array

# Calculate happiness for input arguments.
# cnt_happiness takes the score of happiness
def calculate_happiness(in_array, in_set_a, in_set_b):
  cnt_happiness = 0
  for item in in_array:
    if item in in_set_a:
      cnt_happiness += 1
    else:
      pass
    if item in in_set_b:
      cnt_happiness -= 1
    else:
      pass

  return cnt_happiness

# Show everything about the test.
def output(in_array, in_set_a, in_set_b):
  print( "\n *** OUTPUT *** \n" )
  print( " Array         : ", in_array )
  print( " Set_A         : ", in_set_a )
  print( " Set_B         : ", in_set_b )
  print( " Happiness !!! : ", calculate_happiness(in_array, in_set_a, in_set_b) )
  

if __name__ == "__main__":
  
# Multiple input arguments together.
  n, m = [int(kk) for kk in input(" n and m respectivey : ").split()]  

# w_list is used for input array.
  w_list = []
# w_list = [ int(kk) for kk, ii in zip( input().split(), range(n) ) ]  
# NOTE: 75.line is not enough !! We need an exception or smth else.
  
  w_list = [ int(kk) for kk in input(" input array : ").split() ]    
# Check in_array's conditions it can contains duplicated items but its length 
# ... can not be less or bigger than n.  
  if len(w_list) != n:
    print(" Much or less input arguments detected for w_array !!! ")
    usage()
    sys.exit(-1)
  
# Cast list to nd.array.
  w_array      = np.asarray(w_list)
# Basically create sets with function.
  set_a_array  = create_sets(m)
  set_b_array  = create_sets(m)

# Output func. shows everything about test.
  output(w_array, set_a_array, set_b_array)
