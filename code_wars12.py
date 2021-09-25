def hexx(r, g, b)
    number = r, g, b
    # list of hex number
    lst_dict = {0:"0", 1:"1", 2:"2", 3:"3",
                4:"4", 5:"5", 6:"6", 7:"7",
                8:"8", 9:"9", 10:"A",11:"B",
                12:"C",13:"D",14:"E",15:"F"}
    empty = ""
    # looping through r, g, b
    for n in number:
        # for the minimal number
        if n<0:
            n = 0
        # for the maximum number
        elif n>255:
            n = 255
        # float division the number for the first digit
        first_dig = n//16
        # divide it by 16 and take the decimal, multiply by 16 (ex. 13.35, we want the 0.35)
        second_dig = ((n/16) - n//16)*16
        # taking those number from the dictionary
        complete_dig = lst_dict[first_dig]+lst_dict[second_dig]
        empty+=complete_dig
    

    return(empty)
                

hexx(255,278,252)
