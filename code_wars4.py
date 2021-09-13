def is_isogram(string):
    new_str = string.lower()
    print(new_str)

    count = dict()
    for letter in new_str:
        count[letter] = count.get(letter, 0) + 1
    print(count)

 
    for i, j in count.items():
        if j == 1:
            continue
        elif j != 1:
            return(print(False))
    return(print(True))
            
        
        
is_isogram(" ")
