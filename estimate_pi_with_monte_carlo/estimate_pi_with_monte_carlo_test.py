import random
import math, os, getopt, sys
import numpy as np
import csv

class magic_pi(object):

# Constructor for class.  
  def __init__(self, num_of_total_point):
    self.num_of_total_point = num_of_total_point
    
  def set_total_point(self, in_point):
    self.num_of_total_point = in_point
    
  def estimate_pi(self):
    num_of_points_in_circle = 0
    for kk in range(self.num_of_total_point):
# Changing seed by current time.      
      random.seed()
# Generate a float random number between 0 to 1.
# This coordinates is our random x,y coordinates in the x,y plane. 
      coordinate_x = random.random()
      coordinate_y = random.random()

# Calculating distance point to origin. Using this info we use an approximation.
      distance_to_origin = math.pow(coordinate_x, 2) + math.pow(coordinate_y, 2)
# No need sqrt because sqrt(>1) is bigger than 1.
      distance_to_origin = math.sqrt(distance_to_origin)

# If random point is in circle increase the parameter by 1.
# If not don't do anything.
      if distance_to_origin <= 1:
        num_of_points_in_circle += 1
      else:
        pass
      
# Our circle and rectangle areas relationship.
    approximate_pi = 4 * num_of_points_in_circle / self.num_of_total_point
# Return estimated pi value.
    return approximate_pi    
  
# Checking magic_pi is bigger or less than real pi.
def check_less_or_bigger(in_list):
# How many result is bigger or less than real pi
  big_count = 0
  less_count = 0
# Taking results in list.
# Compare with real pi.
# Return two item for this function it can be possible for python just like that.
  for item in in_list:
    if item > np.pi:
      big_count += 1
    else:
      less_count += 1
  return big_count, less_count

def csv_writer(file_name, in_data):
# Guaranteed the file is created
  os.system("touch %s" % file_name)
  
# With open keyword we append rows to our file.
  with open(file_name, 'w') as ff:
    writer = csv.writer(ff)
    writer.writerow(in_data)

def csv_reader(file_name):
# Basic reader function. This function reads file and yield every each row respectively.
# Every csv_reader function call this file return just one row
  with open(file_name, 'r') as ff:
    reader = csv.reader(ff)
    for row in reader:
      yield(row)

def output(in_list):
# Basic output function for result of all operations.
  print(" \n *** OUTPUT *** \n")
  print( "Remember PI              : ", math.pi )
  print( "Number of total test     : ", len(in_list) )
  print( "Average of results       : ", np.mean( np.asarray(in_list) ) )
  print( "Number of bigger than PI : ", check_less_or_bigger(in_list)[0] )
  print( "Number of less than PI   : ", check_less_or_bigger(in_list)[1] )


def usage():
# Basic usage function.
# This function called when compilation error.
  print("\n *** USAGE *** ")
  print("-o Number_of_Random_Point ")
  
if __name__ == "__main__":
  
# Our file name same directory with our script.
  file_name = "test.cvs"

# Command takes the command line arg.
  command = None

# With try catch block we take argument as we wanted form
  try:
    opts, args = getopt.getopt( sys.argv[1:], "-o:", ["output="] )
    
  except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(-1)

# Input argument form will be like -o num_of_rand_point form.  
# Opts is a tuple we took the second argument of this.
  for out, arg in opts:
    if out in("-o", "--out"):
      command = arg

# If we could not take the num_of_rand_point input argument form probably wrong.
  if command == None:
    print(' Invalid input argument !!!')
    usage()
    sys.exit(-1)

# Cast str to int input argument
  num_of_rand_point = int(command)

# Test instance for class.  
  test_instance = magic_pi(num_of_rand_point)

# Whole magic_pi results which are appended a list iteratively.
# List length will be as long as iteration_num
  list_of_result = []
  iteration_num  = 100
  for kk in range(iteration_num):
    list_of_result.append \
      ( test_instance.estimate_pi() )

# Send results list to the writer function.
# Writes a file row.
  csv_writer(file_name, list_of_result)

# Takes whole results from a file row. 
# Basically show whole result in command prompt
  kk = 0
  for item in csv_reader(file_name):
    for i in item:
      kk += 1
      print(kk, "-> ", i)

  output(list_of_result)
  
