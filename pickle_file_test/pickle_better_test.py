#!/usr/bin/python3

import m_pickle as mp
import os, sys, getopt

'''   
 opts is a kind of list of tuple contains...
 command line arguments these are...
 store, laod_all_print, load_all_cost    

'''

def better_test():
  command = None
  number_of_store = None

 # Path concatination 
  directory_path = 'data_folder' 
  file_path      = '16_02_2021.dat'
  data_path      = '%s/%s' % (directory_path, file_path)
  
  try:
    opts, args = getopt.getopt(sys.argv[1:],  
                               "ho:", 
                               ["help", "output="] )
    
  except getopt.GetoptError as err:
    print(err)
    mp.usage()
    sys.exit(-1)

  for out, arg in opts:
    if out in("-h", "--help"):
      mp.usage()
      sys.exit(-1)
    elif out in ("-o", "--output"):
      command = arg
    else:
      pass
# Alternative : command = opts[0][1]
  
  if command == 'store':
    number_of_store = int(args[0])
    print(' *** STORE CASE *** ')
    print(' number_of_store_item : ', number_of_store)

    list_of_instances = []
    
    for i in range(number_of_store):
      in_id               = input('id         : ')
      in_department       = int(input('Department : '))
      in_hour             = int(input('Hour       : '))
      
      instance = mp.tmpEmployee(in_id ,mp.job_types[in_department], \
        in_hour, mp.hour_per_payment_types[in_department])
      
      list_of_instances.append(instance)
      print('')
    
    mp.write_to_pickle(file_path ,data_path, list_of_instances)
    
  elif command == 'load_all':
    print(' *** LOAD ALL CASE *** ')
    print(" \n *** READ FROM FILE !!! *** \n")
    
    directory_path = 'data_folder'
    
    read_datas = mp.read_from_pickle(data_path)
    mp.print_list(read_datas)
    
  elif command == 'total_cost':
    print(' *** TOTAL COST CASE *** ')
    read_datas = mp.read_from_pickle(data_path)
    total_cost = mp.get_all_cost(read_datas)
    print(' Total cost until now : ', total_cost)
  
  elif command == 'clean':
    print(' *** DELETING FILE *** ')
    os.system('cd data_folder && rm -rf %s' % file_path)
    
  else:
    print(' *** NO SUCH A CHOICE !!! *** ')
    sys.exit(-1)
      
if __name__ == "__main__":
  better_test()

