def delete(order, max_e):
    num_dict = dict()
    for number in order:
        num_dict[number] = num_dict.get(number, 0) + 1

    no_num = None
    num_list = list()
    new_list = list()
    for k, v in num_dict.items():
        if v > max_e:
            numero = [k] * max_e
            for i in numero:
                num_list.append(i)
            
        else:
        
            numero = [k] * v
            for j in numero:
                num_list.append(j)

    return(num_list)
    
    
    


        
            
        
        


delete([1,1,3,3,7,2,20,2,2], 3)
delete([20,37,20,21], 1)
    



            
