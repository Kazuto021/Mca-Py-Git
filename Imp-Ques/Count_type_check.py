def count_check(li):
    dict={"Neg":0,
          "Pos":0}
    for i in li:
        if i<0: dict["Neg"] +=1 
        elif i>0: dict["Pos"] +=1 
        
    return dict
    
    
li = [1,-2,-3,4]

print(count_check(li))
    