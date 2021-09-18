import re
def camel(string):
    # Making sure to return an empty list 
    if len(string) == 0:
        print("")
    else:
        # Get that first letter
        new = string[0]

        # If the first letter is capital....
        if new.isupper():
            # split it with regex
            # it will return a list
            a = re.split("[\-_]", string)
            lst = ""
            for words in a:
                # all of the words starts with capital letter
                new = words.capitalize()
                lst+=new
            print(lst)


        # If the first letter is not capital...
        elif not new.isupper():
            #split it with regex
            # it will return a list
            a = re.split("[\-_]", string)
            lst = ""
            for words in a:
                # all of the words starts with capital letter
                new = words.capitalize()
                lst+=new
            # Make the first letter into lowercase and concatenate it with the rest
            print(lst[0].lower()+lst[1:])

camel("Apple_bottom_jeans_boots_with_the_fur")
camel("i_Wanna_see-your-pick")
camel("bruh_u_be_down_so_bad")
camel("")



    
    




