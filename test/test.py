"""
This is doc:
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""
from datetime import datetime

#print(__doc__)


class WorkStartError(ValueError):
    """This is doc:"""
    pass


class WorkEndError(ValueError):
    """This is doc:"""
    pass


class ObjIter:
    """This is doc:"""

    def __init__(self, data: list):
        """This is doc:"""
        self.data = data

    def __iter__(self):
        """This is doc:"""
        return self

    def __next__(self):
        """This is doc:"""
        if not self.data:
            raise StopIteration
        return self.data.pop(0)


class Factory:
    """This is doc:"""

    def __init__(self, date1, date2):
        """This is doc:"""
        self.date1 = date1
        self.date2 = date2
        self.work = {}
        self.cheating_dict = {}

    def add_work(self, name: str, date: list):
        """This is doc:"""
        for worker_name, worker_data in self.work.items():
            for j in worker_data:
                if j in date:
                    if worker_name == name:
                        raise DuplicateDataException('Duplicate values!')
                    else:
                        date.remove(j)
                        self.work[name] = date
                        list_to_modify = self.work[worker_name]
                        list_to_modify.remove(j)
                        self.cheating_dict[j] = (worker_name, name)
                        raise ValueError(f"Conflict series: {j}, Workers: {worker_name}, {name}")
        self.work[name] = date

    def __iter__(self):
        """This is doc:"""
        result = []
        for v in self.work.values():
            result.extend(v)
        return ObjIter(result)


#form = "%H:%M:%S"
#date_diff = datetime.strptime(Factory.date1, form) - datetime.strptime(Factory.date2, form)

Factory.date1=datetime.date(11,11,11)
Factory.date2=datetime.date(11,11,11)
date_diff=Factory.date2-Factory.date1
print(date_diff)

Factory.add_work('Joe', ['09', '01', '20'])
Factory.add_work('Ana', ['09', '03', '15'])
Factory.add_work('Tim', ['09', '04', '25'])

try:
    Factory.add_work('Tim', ['09', '04', '35'])
except ValueError:
    pass


print(Factory.work)
print(Factory.cheating_dict)
with open('test', 'w') as file:
    for x in Factory:
        file.write(str(x) + "\n")
