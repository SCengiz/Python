#!/usr/bin/python3
import sys

# Base class
class Events:
  pass

# Inherited from Events class. This class uses for even numbers.
class EvenStream( Events ):
# Initially even member must be equal to 2.
  def __init__(self):
    self.even_  = -2 

# get_next function yield +2 version of even parameter.
  def get_next(self):
    self.even_ += 2
    yield self.even_

# Use for odd numbers. Same as Even.
class OddStream( Events ):
  def __init__(self):
    self.odd_ = -1
    
  def get_next(self):
    self.odd_ += 2
    yield self.odd_

# print function has a default Even class arg.
# next keyword helps us for iteratively printing.
def print_from_stream( num, stream = EvenStream() ):
  for _ in range( num ):
    next_item = next( stream.get_next() )
    print( next_item )
  print( "**" )

def usage():
  print("\n *** USAGE *** \n")
  print(" Number of test ->  Test Number ")
  print(" Example : <-  odd 2 & even 3  ->  ")
 
 
if __name__ == "__main__":

# Number of tests parameter.
  num_of_tests = int( input( " -> Test Number : " ) )
  
# We store nums in keys, and the class instances stored in values of dictionary.
  in_dict = {}
# with split keyword we took whole line to 2 arguments.
  for kk in range( num_of_tests ):
    try:
      in_str, in_num = [ ii for ii in input(" -> ").split() ]
      in_num = int(in_num)

      if in_str == "odd" and in_num > 0:
        in_dict[ in_num ] = OddStream()
      elif in_str == "even" and in_num > 0:
        in_dict[ in_num ] = EvenStream()
      else:
        print(" Invalid input arguments ")
        break
    except Exception as err:
      print(" ERROR : ", err)
      usage()
      sys.exit(-1)
    
# Output block for script. 
# If value is EvenStream instance then use one parameter for print_from_stream function
  for item in in_dict.keys():
    even_flag = isinstance( in_dict[item], EvenStream )
    if even_flag:
      print_from_stream( item )
    else:
      print_from_stream( item, in_dict[item] )
    
