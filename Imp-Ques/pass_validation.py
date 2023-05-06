pwd=input("Enter the password:\n")

di={}
itr=0

def length_check(string):
    if len(string)<16 and len(string)>6:
        print("\nPassword length : Valid.")
        di["Length Check"] = True
        return 1
    di["Length Check"] = False
    return 0
    
def special_check(string):
    char_array = ["$","#","@"]    
    for i in char_array:
        if i in string:
            print(f'Special character "{i}":Valid')
            di["Special Check"] = True
            return 1
    di["Special Char"] = False
    return 0
    
def num_char_check(string):
    
    di["Num Check"] = False
    di["Lower Case"] = False
    di["Upper Case"] = False   
    for i in string:
        asci = ord(i)
        if asci >=48 and asci<=57:
            di["Num Check"] = True
        elif asci >=97 and asci <=122:
            di["Lower Case"] = True
        elif asci >=65 and asci<=90:
            di["Upper Case"] = True

    print(f'Num-Check:{di["Num Check"]}\nLower-Case-Check:{di["Lower Case"]}\nUpper-Case_check:{di["Upper Case"]}')
    return di["Num Check"],di["Lower Case"], di["Upper Case"]
    

li = [length_check(pwd),special_check(pwd),num_char_check(pwd)]

for key in di:
    valid = 1
    if di[key] != True:
        print("\nInvalid Password!")
        print("Error=>",key,":",di[key])
        valid = 0
        break
    elif itr == len(di)-1 and valid ==1:
        print("Valid Password.")
        
    itr+=1
    