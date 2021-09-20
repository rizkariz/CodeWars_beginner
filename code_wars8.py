def roman(n):
    one = 'I'
    five = 'V'
    ten = 'X'
    fifty = 'L'
    onehundo = 'C'
    fivehundo = 'D'
    thousand = 'M'

    # turning n(integer) into string 
    new_num = str(n)
    

    # Making a list from the string
    lis_num = list()
    for i in new_num:
        lis_num.append(i)
        

    # Finding the length of the list
    a = len(lis_num)


    # determining the thousands, hundreds, tens, and ones based on the length
    if a == 2:
        d_thousands = 0
        c_hundreds = 0
        b_tens = int(lis_num[0])
        a_ones = int(lis_num[1])
    elif a == 3:
        d_thousands = 0
        c_hundreds = int(lis_num[0]) 
        b_tens = int(lis_num[1]) 
        a_ones = int(lis_num[2])
    elif a == 4:
        d_thousands = int(lis_num[0]) 
        c_hundreds = int(lis_num[1]) 
        b_tens = int(lis_num[2]) 
        a_ones = int(lis_num[3])
    
    elif a == 1:
        d_thousands = 0
        c_hundreds = 0
        b_tens = 0
        a_ones = int(lis_num[0])
        
        
        
    
    #---------------------------------------------------------#



# for thousands
    d = d_thousands
    if 1 < d <= 3:
        d_num = thousand * d
    elif d == 1:
        d_num = thousand
    else:
        d_num = ""

# for hundreds
    c = c_hundreds
    print(c)
    if c <= 3:
        c_num = onehundo * c
        
    elif c == 4:
        c_num = onehundo+fivehundo
    elif c == 5:
        c_num = fivehundo
        
    elif c == 9:
        c_num = onehundo + thousand
        
    elif 5 < c <= 8:
        c_cnum = c - 5
        c_num = fivehundo + onehundo *(c_cnum)
        print(c_cnum)
        print(c_num)
    else:
        c_num = ""



        
# for tens
    b = b_tens
    if b <= 3:
        b_num = ten * b   
    elif b == 4:
        b_num = ten + fifty
    elif b == 5:
        b_num = fifty    
    elif b == 9:
        b_num = ten + onehundo   
    elif 5 < b <= 8:
        b_bnum = b - 5
        b_num = fifty + ten *(b_bnum)
        
    else:
        b_num = ""

# for ones
    if 1<= a_ones <= 3:
        a_num = one * a_ones
        a_num = str(a_num)
    elif a_ones == 4:
        a_num = one + five      
    elif a_ones == 5:
        a_num = five     
    elif 5 < a_ones <= 8:
        a_num = five + one * (a_ones-5)  
    elif a_ones == 9:
        a_num = one + ten
    else:
        a_num = ""
        



    return(print(d_num + c_num + b_num + a_num))
   



   
    
     



roman(1509)
roman(3452)
        






    
