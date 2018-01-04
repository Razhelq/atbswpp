# Comma code - Converts a list to a string.

spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(da_list):
    new_string = ""
    for i in range(len(da_list)):
        if da_list[i] != da_list[-2] and da_list[i] != da_list[-1]:
            new_string += da_list[i] + ", "
        if spam[i] == spam[-2]:
            new_string += da_list [i] + " and "
        if spam[i] == spam[-1]:
            new_string += da_list[i]
    return new_string

code = comma_code(spam)        
print(code)







    
