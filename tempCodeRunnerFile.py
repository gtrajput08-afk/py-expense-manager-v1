print("|| Expense Manager ||")
expenses=[]

count=1
while count<=2:
 exp_name=input("Enter expense name : ")
 amount=float(input("Enter expense amount : "))
 info={
 "Name":exp_name,
 "Amount":amount
}
 expenses.append(info)
 count=count+1
try:
 print(expenses)
 discount_per=int(float(input("Enter discount percentage : ")))
 if (amount>0 and 0<=discount_per<=100):
  print(f"Expense : {exp_name}")
  print(f"Amount : Rs.{amount}")
  discount=(amount*discount_per)/100
  final_amount=amount-discount
  print(f"Discount {discount_per}% : Rs.{discount}")
  print(f"Final Amount : Rs.{final_amount}")
 else:
  print("NOTE : Amount must be greater than 0 and discount must be between 0 and 100.")  
except ValueError:  
 print("Invalid input ! Please enter a valid number.") 