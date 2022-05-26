#Chapter 17 pg. 111

# 17.0 function definition
def add_2(num):
    """
    return 2 more than num
    """
    result = num + 2
    return result

# 17.2 Global & local scope
x = 2 #Global
def scope_demo():
    y = 4 #Local
    print("Local: {}".format(y))
    print("Global: {}".format(x))
    print("Built-in: {}".format(dir))
scope_demo()

# 17.3 Multiple Parameters
def add_two_nums(a, b):
    return a + b

# 17.4 Default Parameters
def add_n(num, n=3):
    """default to adding 3"""
    return num + n
    #to create a def val for param. follow param name by an '=' then a chosen value.