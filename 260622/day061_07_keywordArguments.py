def print_kwargs(**para):
    print(para)
print_kwargs(a=1)
print_kwargs(name='foo', age=3) #이전버전에서는 key값이 자동sorted 되었음 지금은 안되는듯?