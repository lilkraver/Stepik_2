def closest_mod_5(x):
    if x % 5 == 0:
        print(x)
    else:
        while x % 5 != 0:
            x += 1
    return x    
