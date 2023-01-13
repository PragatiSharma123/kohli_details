#from employee import employee_list,get_employee_address_details
#print (employee_list)
from employee import *
employee_addr_list = get_employee_address_details(employee_list,key="pincode")
print(employee_addr_list)