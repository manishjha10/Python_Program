class Solution :
  def sortRecords(self , employee, salary):
     # first zipped the employee and salary in tuple 
     zipped =  list(zip(employee, salary)) 
    # sort according to the salary and multiple salary sort by employee
     sorted_names_employee  =  sorted(zipped ,key = lambda :x (x[1] ,x[0]) 
     # x[1]  sort the salary basics sort and having two employee samesalry the sort according to the x[0]  names basics sort 
     # unzipped  takes two argument 
     result , _  =  zip(*sorted_names_employee)   
     return result 
                                        
