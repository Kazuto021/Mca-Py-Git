def multi(k:int):
    checker = 0 
    # breaker = ""
    
    while checker < k:
        li=[]
        for i in range(1,6):
            li.append(k*i)
        
        print("Program completed.")
        return li
        # breaker = input("Type 'done' to exit.\n")
        
        # if breaker == "done":
        #     return
    return "Negative value of 'k' is selected. Please select +ve value and try again"

print(multi(int(input("Enter a +ve value of 'k':\n"))))