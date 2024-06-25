
obj = 1000
for name in dir(obj):
    value = getattr(obj,name)
    print(f"{name} {value} callable : {callable(value)}")
print(f" getattr(obj, 'bit_length')() is {getattr(obj, 'bit_length')()}")
print(f" getattr(obj, 'as_integer_ratio')() is {getattr(obj, 'as_integer_ratio')()}")
