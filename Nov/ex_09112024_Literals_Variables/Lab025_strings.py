from traceback import format_stack

name = "this is big line"
print(type(name))
name = name + str(1) # can only concatenate str ( not "int") to str
print(name)

first_name = "rakesh"
last_name = "ind"
full_name = first_name+" "+last_name
print(full_name)
print(type(full_name))