#!/usr/bin/python3
import sys

# A class definition for operations !!!
class EventStream( object ):
  
# Class has 2 member variable.
  def __init__ (self, stream, num):
    self.stream_ = stream 
    self.num_    = num

# Basically using "yield" keyword we do our job.  
# Like ternary operator. One line if-else block.
  def get_next(self):
    kk = 0 if self.stream_ == "even" else 1
    num = self.num_    
    while num > 0:
      yield kk
      kk += 2         
      num -= 1

# Printing numbers 0 or 1 to num.    
def print_from_stream( stream ):
  for kk in ( stream.get_next() ):
    print( kk )
  print(" ** ")
    
def usage():
  print("\n *** USAGE *** \n")
  print(" Number of test ->  Test Number ")
  print(" Example : <-  odd 2 & even 3  ->  ")
  
  
if __name__ == "__main__":
  
# Test instances will be stored to list
  list_instances = []
# Taking number of test here !!
  num_of_tests = int( input(" -> Test number : ") )
# num_of_tests times we do same job.
# try-catch block is checking our input parameters.
  while num_of_tests > 0:
    try:
      in_str, in_num = [ kk for kk in input(" -> ").split() ]
      if in_str == "odd" or in_str == "even":
        test_instance = EventStream( in_str, int( in_num ) )
        list_instances.append( test_instance )
      else:
        break
    except Exception as err:
      print(" ERROR : ", err)
      usage()
      sys.exit(-1)
    num_of_tests -= 1

# Print whole instances results.
  for item in list_instances: 
    print_from_stream( item )
