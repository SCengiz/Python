import modules.submodule_1 as sm1
import modules.submodule_2 as sm2

sm_list = [[sm1, 1], [sm2, 2]]

print(' ** Submodule Functions ** ')

for item in sm_list:
    print("Number from submodule_" + str(item[1])  
          + ":\n" , item[0].get_number())
print('')

print(' ** Circle Class ** ')

radius = 10
circle_instance = sm1.Circle(radius)
print("Radius of Circle : ", radius)
print("Area of circle   : ", circle_instance.area() )
print('')

print(' ** Employee Class ** ')

employee_instance = sm2.Employee("Name", "Surname", 1000)
employee_instance.displayEmployee()
print('')

employee_instance_2 = sm2.Employee("Name", "Surname", 2000)
employee_instance_2.displayEmployee()
print('')

print('  ** Total Costs **  ')

employee_instance_2.displayCount()
employee_instance_2.displaySalary()

