from ast import Lambda
from gettext import find
from operator import truediv
from traceback import print_list

class Underscore:
    def map(self, iterable, callback):
        print(list(map(callback, iterable)))
    
    def find(self, iterable, callback):
        pass

    def filter(self, iterable, callback):
        print(list(filter(callback, iterable)))
        

    def reject(self, iterable, callback):
        pass

_ = Underscore()
_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
_.map([1,2,3], lambda x: x*2) 
_.find([1,2,3,4,5,6], lambda x: x > 4)


#_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
#_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]







