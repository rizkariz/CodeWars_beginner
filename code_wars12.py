def hexx(r, g, b):
    number = r, g, b
    lst_dict = {0:"0", 1:"1", 2:"2", 3:"3",
                4:"4", 5:"5", 6:"6", 7:"7",
                8:"8", 9:"9", 10:"A",11:"B",
                12:"C",13:"D",14:"E",15:"F"}
    empty = ""
    for n in number:
        if n<0:
            n = 0
        elif n>255:
            n = 255
        first_dig = n//16
        second_dig = ((n/16) - n//16)*16
        complete_dig = lst_dict[first_dig]+lst_dict[second_dig]
        empty+=complete_dig
    

    return(empty)
                

hexx(255,255,252)
