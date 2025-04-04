def GCD (m , n ):
    if m == 0:
        print(f"GCD: {n}")
    if n == 0:
        print(f"GCD: {m}")
    else:
        while n != 0:
            r = m % n
            m = n 
            n = r
        print(f"GCD : {m}" )

GCD(24,9)