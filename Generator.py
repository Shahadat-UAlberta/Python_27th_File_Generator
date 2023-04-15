"""
- Generator Function
- Normal Function: return || Generator Function: yield
"""
"""
def getListValue(lst):
    return lst 


lst = [1,2,3,4]
print(lst)
"""


def generator_function():

    yield "Hello World"
    yield (1, 2, 3, 4)
    yield [1, 2, 3, 4]


func = generator_function()
print(func)  # <generator object generator_function at 0x0000018B573CB8A0>

print(next(func))
print(next(func))
print(next(func))
print(next(func))
