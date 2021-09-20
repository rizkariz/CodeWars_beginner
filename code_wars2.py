def get_sum(a, b):
    count = 0
    if a == b:
        return(print(a))
    elif a < b:
        for num in range(a, b+1):
            count+=num
        print(count)
    elif b < a:
        for num in range(b, a+1):
            count+=num
        print(count)
           
get_sum(5, -9)
