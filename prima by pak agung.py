def is_prima(num):
    _count = 0
    for x in range(1, num+1):
        if (num % x == 0):
            _count =+ 