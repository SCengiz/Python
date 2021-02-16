#!/usr/bin/python3

import pickle
import os

class Employee(object):    
    pass

 # A class definition for object storing  

class tmpEmployee(Employee):  
  # Constructor
  def __init__(self, id_, department_, hour_, hour_per_payment_):
    self.id_ = id_
    self.department_ = department_
    self.hour_ = hour_
    self.hour_per_payment_ = hour_per_payment_

  # Operator Overload
  def __str__(self):
    return ' id : {} \n Department : {} \n Hour : {} \n Hour_per_payment : {}' \
      .format(self.id_, self.department_, self.hour_, self.hour_per_payment_)
      
  def calculate_daily_pay(self):
    payment = self.hour_ * self.hour_per_payment_
    return payment
  
 # You can change these as you wish
job_types \
    = {
        0 : 'Department_0', 
        1 : 'Department_1', 
        2 : 'Department_2',
        3 : 'Department_3',
        4 : 'Department_4',
      }

hour_per_payment_types \
  = {
      0 : 5,
      1 : 10,
      2 : 12,
      3 : 15,
      4 : 25,
    }

 # Calculating all the cost until now
def get_all_cost(in_list):
  copy_list = in_list
  total_cost = 0
  for item in copy_list:
    total_cost += item.calculate_daily_pay()
  return total_cost
  
def usage():
  print(' *** HELP *** ')
  print('using    : python3 script_name -o & --output commands')
  print('commands : \n 1.store \n 2.load_all \n 3.total_cost \n 4.clean ')
  
 # Write to the file 
def write_to_pickle(file_path, data_path, in_list):
  os.system('mkdir -p data_folder')
  os.system('cd data_folder && touch %s' % file_path)
  with open(data_path, 'ab') as fin:
    for item in in_list:
      pickle.dump(item, fin)

 # Read from the file 
def read_from_pickle(file_path):
  read_datas = []
  with open(file_path, 'rb') as fout:
    while True:
      try:
        read_datas.append(pickle.load(fout))
      except:
        break
  return read_datas

 # Basic print list types function
def print_list(in_list):
  i = 1
  for item in in_list:
    print(str(i) + ".instance")
    print(item)
    print(" Daily payment : ", item.calculate_daily_pay())
    i += 1
