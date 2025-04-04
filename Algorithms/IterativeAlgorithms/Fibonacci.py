def fibonnaci(n):
    first = 0 
    second = 1
    i = 3 
    while i <= n:
        temp = first +second 
        first = second 
        second = temp
        i += 1
        print(temp)

fibonnaci(5)