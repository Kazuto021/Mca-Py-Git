def multi(k:int):
    checker = 0 
    
    while checker < k:
        li=[]
        for i in range(1,6):
            li.append(k*i)
        
        print("Program completed.")
        return li
    
    return "Negative value of 'k' is selected. Please select +ve value and try again"

print(multi(int(input("Enter a +ve value of 'k':\n"))))