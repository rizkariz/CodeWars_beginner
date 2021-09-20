def question(var_1, var_2):
    var_1 = list(var_1)
    print(var_1)

    var_2 = list(var_2)
    print(var_2)

    var_12 = list(set(var_1 + var_2))

    var_12.sort()
    var_12 = "".join(var_12)

    return(print(var_12))

question("imherewithyou", "ohbabyimissyoudemn" )

