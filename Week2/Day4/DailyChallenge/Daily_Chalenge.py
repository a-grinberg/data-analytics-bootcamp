
def divide_by_zero(a, b):
    try: x = a/b
    except ZeroDivisionError:
        print(f"You can't divide by zero." )
    except TypeError:
        print(f' a and b should be only int.')
    

divide_by_zero(5, 0)
divide_by_zero('5', 0)
