def square(nums):
    for num in nums:
        yield num ** 2


nums = [10, 20, 30, 40, 50]
gen_func = square(nums)
print(gen_func)

print(next(gen_func))
print(next(gen_func))
print(next(gen_func))
print(next(gen_func))
print(next(gen_func))
