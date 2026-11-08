total=0
while True:
  print("Happy Restaurant")
  print("1. Burger-Rs.120")
  print("2. Pizza-Rs.200")
  print("3. Sandwich-Rs.80 ")
  print("4. French Fries-Rs.60")
  print("5. Cold Drink-Rs.40")
  print("6. Finish Order")
  choice=int(input( "Enter your choice:"))
  if choice==6:
        print(f"total amount={total}")
        print(f"Discount={discount}")
        print(f"Discount Percentage={discount_percentage}")
        print(f"Final Bill:{total-discount_percentage}")
        print("Thanks for visiting!")
        break
  elif 1<=choice<=5:
        print("Valid choice") 
       
        quantity=int(input("Enter Quantity"))
        if quantity<1:
               print("Invalid Quantity")
        else:
         print("Valid Quantity")
         
    
         if choice==1 :
            print("Item=Burger")
            print(f"Cost={120}")
            print(f"total_cost1={120*quantity}")
            total_cost1=120*quantity
            total=total+total_cost1
         elif  choice==2:
                        print("Item=Pizza")

                        print(f"Cost={200}")
                        print(f"total_cost2={200*quantity}")
                        total_cost2=200*quantity
                        total=total+total_cost2
         elif choice==3:
                                    print("Item=Sandwich")
                                    print(f"Cost={80}")
                                    print(f"total_cost3={80*quantity}")
                                    total_cost3=80*quantity
                                    total=total+total_cost3                            
         elif choice==4:
                                                print("Item=French Fries")
                                                print(f"Cost={60}")
                                                print(f"total_cost4={60*quantity}")
                                                total_cost4=60*quantity
                                                total=total+total_cost4
         else:
                                                            print("Item=Cold Drink")
                                                            print(f"Cost={40}")
                                                            print(f"total_cost5={40*quantity}")
                                                            total_cost5=40*quantity
                                                            total=total+total_cost5
         if total<500:
                                 discount=0
                                 discount_amount=total*discount
                                 discount_percentage=(discount_amount)/(100)
                                 
         elif total>=500 and total<=999:
                                 discount=5
                                 discount_amount=total*discount
                                 discount_percentage=(discount_amount)/(100)
         else:      
                                  discount=10
                                  discount_amount=total*discount
                                  discount_percentage=(discount_amount)/(100)        
                                                        
  else:
        print("Invalid choice")       

    
          

