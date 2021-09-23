def hex(n):
    lst_dict = {13: "D", 12: "C"}

    first_dig = n//16
    second_dig = ((n/16) - n//16)*16 

    hex_number = lst_dict[first_dig] + lst_dict[second_dig]
    print(hex_number)

hex(220)
