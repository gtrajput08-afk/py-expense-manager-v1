"""LIST TEST"""
# expenses=[]
# expenses.append("Food")
# expenses.append("Travel")
# print(expenses)

"""WHILE LOOP TEST"""
# num=1

# while (num<=5):
#     print(num)
#     num=num+1

"""TRY-EXCEPT TEST"""
# try:
#     age=int(input("Enter your age : "))
#     print(f"Age : {age}")
# except ValueError:
#     print("Please enter a valid number")    

"""DICT CHECK"""
# expenses=[]
# exp={
#     "name":"Food",
#     "amount":250
# }
# expenses.append(exp)
# print(expenses)

"""MULTIPLE EXPENSES + FOR LOOP"""
expenses=[]
food={
    "Food":250,
}
travel={
    "Travel":100,
}
expenses.append(food)
expenses.append(travel)
for expenses in expenses:
 for key,value in expenses.items():
    print(f"Name : {key}\nAmount : {value}")
