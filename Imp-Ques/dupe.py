li=[1,2,3,4,5,6,8,9]

    
def check_duplicate(lst):
    lst = sorted(lst)
    li2 = list(set(lst))
    if lst == li2:
        return(False, "Every element is Unique!")
    else: return(True, "The list contains duplicate...")
    
print(check_duplicate(li))