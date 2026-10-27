print("|| Expense Manager ||")
expenses=[]
try:
 total_expenses=int(input("How many expenses you want to enter ?\nAnswer : "))
 count=1
 while count<=total_expenses:
  exp_name=input("Enter expense name : ")
  amount=float(input("Enter expense amount : "))
  info={
  "Name":exp_name,
  "Amount":amount
  }
  expenses.append(info)
  count=count+1
 print(expenses)
 discount_per=int(float(input("Enter discount percentage : ")))
 total_expense=0

 for expense in expenses:
  print(f"Name : {expense['Name']}")
  print(f"Amount : Rs.{expense['Amount']}")

  if (expense['Amount']>0 and 0<=discount_per<=100):
    discount=(expense['Amount']*discount_per)/100
    final_amount=expense['Amount']-discount
    total_expense=total_expense+final_amount
    print(f"Discount {discount_per}% : Rs.{discount}")
    print(f"Final Amount : Rs.{final_amount}")
  else:
    print("NOTE : Amount must be greater than 0 and discount must be between 0 and 100.")  
 print(f"Total Expense : Rs.{total_expense}")    
except ValueError:  
 print("Invalid input ! Please enter a valid number.") 