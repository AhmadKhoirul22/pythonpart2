def int_within_bounds(n,lower,upper):
    if n > lower and n< upper and type(n) == int:
        return True
    else :
        return False
print (int_within_bounds(3,1,9))
print (int_within_bounds(6,1,6))
print (int_within_bounds(4.5,3,8))