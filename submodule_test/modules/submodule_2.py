#!/usr/bin/python3

def get_number():
		print(' -- Submodule_2 -- ')
		return 2

class Employee(object):
    
    empCount = 0 
    tot_salary = 0
    
    def __init__(self, name, surname, salary):
        self.name    = name 
        self.surname = surname
        self.salary  = salary
        Employee.empCount += 1
        Employee.tot_salary += self.salary
				        
    def displaySalary(self):
    	  print("Total Salary %d" % Employee.tot_salary)
      
    def displayCount(self):
        print("Total Employee %d"  % Employee.empCount)
    
    def displayEmployee(self):
        print(" Name    : ", self.name, "\n", \
              "Surname : ", self.surname, "\n", \
              "Salary  : ", self.salary)
        


