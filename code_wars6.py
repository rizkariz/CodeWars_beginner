def solution(string, ending):
    lg_ending = len(ending)
    if string == '' or ending == '':
        return(print(True))
    elif string[-lg_ending:] == ending:
        return(print(True))
    
    else:
        return(print(False))



solution('ja', 'ninja')
