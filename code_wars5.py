import math
def comp(a, b):
    list_sqrtB = []
    length_a = len(a)
    length_b = len(b)
    for num in b:
        if length_b == 0:
            print("nice")
            return(print(False))
        else:
            number = int(math.sqrt(num))
            list_sqrtB.append(number)
        
                


    
    a = sorted(a)
    b = sorted(list_sqrtB)
    print(b)
    print(a)

    if a != b:
        print("yo")
        return(print(False))
    elif len(a) == 0:
        print(len(b))
        print("nay")
        return(print(False))
    elif a == b:
        print("ey")
        return(print(True))
        
    else:
        return(print(False))
    


    
        
comp({1, 2}, {1, 2})
comp([11,121, 144, 19, 161, 19, 144, 19], [121, 14641, 20736, 361, 25921, 361, 20736, 361])
comp([], [])
comp([121, 144, 19, 161, 19, 144, 19, 11, 110,110], [121, 14641, 20736, 361, 25921, 361, 20736, 361, 220])
    
