""" monkey patch refers to dynamic (or run-time) modifications of a class or module

1. Use if you have a really good reason(like - temporary critical hotfix)
2. Write proper documentation describing the reason for monkey patch
3. Documentation should contain the information about the removal of the monkey patch and what to watch for. Lots of monkey patches are temporary, so they should be easy to remove.
4. Try to make monkey patch as transparent as possible also place monkey patch code in separate files

"""
print("___________________________Example 1________________________________")
import monk

def monkey_f(self):
    print('monkey_f() called')

#replaceing address of func() with monkey_f()
monk.A.func = monkey_f
obj= monk.A()

#calling function func whose add got replaced with func monkey_f
obj.func()

print("___________________________Example 2________________________________")

class MonkeyPatch():
    def __init__(self,num):
        self.num = num

    def addition(self,other):
        return (self.num + other)

obj1 = MonkeyPatch(10)
add_func = obj1.addition(20)
print(add_func)

import inspect
print(inspect.getmembers(obj1, predicate=inspect.ismethod))


def subtraction(self,num2):
    return (self.num - num2)

MonkeyPatch.subtraction = subtraction
print("------------------------------After MonkeyPatch----------------------------")
print(inspect.getmembers(obj1, predicate=inspect.ismethod))

