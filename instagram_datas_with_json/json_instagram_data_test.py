"""
  INSTAGRAM DATAS
"""

#!/usr/bin/python3

import numpy as np
import sys, os
import json

# A function that uses for reading json type file.
def read_from_json(file_path):
  print('\n READING HERE !!! \n' )
# File operations(opening, control, closing etc) done thanks to open keyword.
# We take the datas in file and save to a dictionary.
  with open(file_path, 'r') as fin:
    dict_datas = json.load(fin)
  return dict_datas

# A help function for usaing this script.
def show_usage(in_pair):
  print(' *** USAGE *** ')
  len_of_pair = len(in_pair)
  for i in range(len_of_pair):
    print(i, ' -> ', in_pair[i])

# Instructions for file topics. 
def print_topic(dict_data, keys_pair, in_command):
  print(" << ", keys_pair[in_command], " >> ")

# To use the data in for loop we need to convert dict to list.
  list_data_topic = list(dict_data[ keys_pair[in_command] ]) 
  len_of_data_topic = len(list_data_topic)
  
# nested for parameters item, cnt.
  [print(cnt+1, ':', item) for item, cnt \
      in zip(list_data_topic, range(len_of_data_topic))]

def print_list(in_list):
  cnt = 1
  for i in range(len(in_list)):
    print(cnt, ":", in_list[i])
    cnt += 1
    
# Command will use befor for a global variable
# None type command must be choosen.
command = None

def conections_test(dict_data, keys_pair):
  print('\n *** CONNECTIONS TEST *** \n')
      
#NOTE: Update this block try-except block get rid of global variable
  try:
    global command
    command = int(input(' Please enter a topic number : '))
  except Exception:
# Exception for invalid input arguments.
    print(' Please give an integer not character or sometihng else !!! ')
    sys.exit(1)
  else:
# Exception for bigger input arguments maybe this block is unnecessary.
    if command >= len(keys_pair):
      print(' Cannot bigger than len of usage !!! ')
      sys.exit(1)
 
  print_topic(dict_data, keys_pair, command)
 
def mutual_follow_check_all(dict_data, keys_pair):
  print('\n *** MUTUAL FOLLOW CHECK ALL TEST *** \n')
# Topics in the conenction.json 5 and 6.
  followers = list(dict_data[ keys_pair[5] ])
  following = list(dict_data[ keys_pair[6] ])
# Sorting the datas for quick comparison.
  followers.sort()
  following.sort()
# List type variable for holds user information that does not follow you.   
  not_follow_to_you = []
# Basic comparison algorithm.
  for item in following:
    if item not in followers:
      not_follow_to_you.append(item)
    else:
      pass
  
  print_list(not_follow_to_you)
  
def mutual_follow_check_one(dict_data, keys_pair, keyword):
  print('\n *** MUTUAL FOLLOW CHECK ONE TEST *** \n')

  followers = dict_data[ keys_pair[5] ]
  following = dict_data[ keys_pair[6] ]
# Specific user check
  if keyword not in list(following):
    print(' You entered wrong instagram user name !!! ')
    sys.exit(-1)
# Note Update this block !!
  try:
    print('Date of you follow to', keyword, ":", following[keyword])
    print("Date of", keyword, "follow to you", ":", followers[keyword])
  except:
    print(' NOT FOLLOWING TO YOU !!! ')
  else:
    print(' FOLLOWING TO YOU !!! ')

"""
        INSIDE
  keys_in_pair =\ 
    {
      0 : 'first_name'
      1 : 'last_name'
      2 : 'contact'
      3 : 'imported_time'  
    }
NOTE: We will use first three  
"""

def all_phone_number():
  print('\n *** ALL PHONE NUMBER TEST *** \n')
  
  file_path = "soraycengiz_20210216/uploaded_contacts.json"
  data_in_list_of_dict = read_from_json(file_path)
  
  keys_in_list = \
    list(data_in_list_of_dict[0].keys())
  
  keys_in_pair = {}
  for i in range(len(keys_in_list)):
    keys_in_pair[i] = keys_in_list[i]
  
#NOTE: Look up to line 105

# Sorting the names
  list_of_list = []
  for i in range(len(data_in_list_of_dict)):
    inside_dict = data_in_list_of_dict[i]    
    inside_list = []

    inside_list.append(inside_dict[ keys_in_pair[0] ])
    inside_list.append(inside_dict[ keys_in_pair[1] ])
    inside_list.append(inside_dict[ keys_in_pair[2] ])
    
    list_of_list.append(inside_list)
# A ranking is designed by looking at the names. x[0] holds the name parameters.
  sorted_list_of_list = sorted(list_of_list, key = lambda x : x[0])
# Index and Range based for together.
  cnt = 0
  for i in range(len(sorted_list_of_list)):
    in_list = sorted_list_of_list[i]
    print("First and Last name    : "\
      , in_list[0], in_list[1])
    print("Phone Number           :"\
      , in_list[2])
    cnt += 1
  
  print('Total phone number >> ', cnt)
  
  
if __name__ == "__main__":
# TESTS 
  
  tests = \
    {
      0 : " conections_test " ,
      1 : " mutual_follow_check_all " ,
      2 : " mutual_follow_check_one " ,
      3 : " all_phone_number " ,
    }
# Display the usage for the user.
  show_usage(tests)  
  test_num = int(input(' Which test do you want : '))

# File path for your connections.json file.
# file_path = "/home/soray/Desktop/Python_Examples/HWTC11/soraycengiz_20210216/connections.json";
  file_path = "soraycengiz_20210216/connections.json"
# Read from connections.json
  data_in_dict = read_from_json(file_path)

# Taking the keys to the empty list
  keys_in_list = []
  keys_in_list = list(data_in_dict.keys())  
  
  keys_in_pair = {}
  for i in range(len(keys_in_list)):
    keys_in_pair[i] = keys_in_list[i]    

  if test_num == 0:
    show_usage(keys_in_pair)
    conections_test(data_in_dict, keys_in_pair)
  elif test_num == 1:
    mutual_follow_check_all(data_in_dict, keys_in_pair)
  elif test_num == 2:
    keyword = 'alperkoose'
    mutual_follow_check_one(data_in_dict, keys_in_pair, keyword)  
  elif test_num == 3:
    all_phone_number()
  else:
    print(' WRONG INPUT ')
    sys.exit(-1)

  
