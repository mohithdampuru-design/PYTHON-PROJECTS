while True:
    budget=int(input("Enter your daily budget:"))
    totals=0
    expenses=0   
    if budget>0:
        print("Valid Budget!")
    else:
        print("Invalid Budget") 
   
    print(" *** Daliy Expenses Recorder *** ")
    print("1.Add an expense ")
    print("2.View total amount spent")
    print("3.View remaining budget")
    print(" 4.View no.f expenses")
    print("5.Exit")
    choice=int(input("Enter your choice"))
    if choice>=1 and choice<=5:
        print("Valid Choice")
    else:
        print("Invalid! Choice")    
    if choice==1:
        print("1.Food")
        print("2,Transport")
        print("3.Study materials")
        print("4.Others")
        amount1=int(input("Enter expenses amount:"))
        expenses+=1
        if amount1>0:
            print("Expense Accepted") 
        amount2=int(input("Enter second Expenses:"))
        
        totals=amount1+amount2
        print(f"First Expense={amount1}")
        print(f"Second_Expense={amount2}")
        print(f"Budget={budget}")
        print(f"total amount spent={totals} ")   
        print(f"Remaining={budget-totals}") 
        expenses+=1
        print(f"No.f expenses={expenses}")
        if budget<totals:
             print("Warning!Your spending has crossed your limit")
        else:
             print("Your spending is normal") 
        break         
    
        
    else:
            print("Invalid Amount")






