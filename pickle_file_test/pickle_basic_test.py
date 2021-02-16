#!/usr/bin/python3

import m_pickle as mp

def basic_test():
  print(" *** BASIC_TEST ***")
  list_of_instances = []

  list_of_instances \
    = [ mp.tmpEmployee("0x01", mp.job_types[0], i+1,mp. hour_per_payment_types[0]) \
        for i in range(5) ]
   
  mp.write_to_pickle('data_folder/qq.dat', list_of_instances)

  print(" \n *** READ FROM FILE !!! *** \n")
  
  read_datas = mp.read_from_pickle('data_folder/qq.dat')
  mp.print_list(read_datas)

if __name__ == "__main__":
  basic_test()
  
