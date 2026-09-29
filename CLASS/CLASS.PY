# 1
# try:
#         a=int(input())
#         b=int(input())
#         print(a/b)
# except ValueError:
#         print("Do not divide by text!!!")
# except ZeroDivisionError:
#         print("Do not divide by zero")
# finally:
#         print("Calculation finished!!!")   




# 2
# try:
#     print("Cities:['Dushanbe', 'Khujand', 'Bokhtar']")
#     a=['Dushanbe', 'Khujand', 'Bokhtar']
#     for i in a:
#         print(a[int(input())])
        
# except IndexError:
#     print("Position does not exist")





# 3
# price={
#        'mouse': 100,
#        'keyboard': 250,
#        'monitor': 1200
#            }
# try:
#     print("Prices:",price)
#     text=str(input())
#     iniger=int(input())
#     print("Total:", price[text]*iniger)
# except KeyError:
#     print("None name")
# except ValueError:
#     print("Print number")







# 4
# def calculate(values):
#     try:
#         l=[]
#         for i in values:
#             l.append(int(i))
#         print(sum(l)/len(l))
#     except ValueError as error:
#         print(error)
#     except ZeroDivisionError as error:
#         print(error)

# k=input().split()
# calculate(k)







 # 5
# def register(name, age):
#     if type(name)==int:
#         raise TypeError("Name must be a string")
#     if type(age)==str:
#         raise TypeError("Age must be a string")
#     if age<18 or age>100:
#         raise ValueError("Age must be from 18 to 100")
#     if name == "":
#         raise ValueError("Name must not be empty")
#     return {"name":name, "age":age}

# while True:
#  try:
#     naem, age=input().split()
#     ag=int(age)
#     print("Registered:", register(naem, ag))
#  except TypeError as error:
#     print("TypeError:", error)
#  except ValueError as error:
#     print("Valuerror:", error)






# 6
# ????????????????







# 7
# class InsufficientFundsError(Exception):
#     def __init__(self, balance, amount):
#         message = f"Insufficient funds: attempted to withdraw  {amount}, but the balance is {balance}."
#         super().__init__(message)

# def process_payment(balance, amount):
#     if amount<0:
#         raise ValueError("Amount must not be negative")
#     if balance<amount:
#         raise InsufficientFundsError(balance, amount)
#     print("New balance:", balance-amount)
    

# try:
#     balan=int(input("Balance: "))
#     pay=int(input("Peyment: "))
#     process_payment(balan, pay)
# except ValueError as error:
#     print(error)
# except InsufficientFundsError as error:
#     print(error)
# finally:
#     print("Payment attempt finished!")





# 8
# def price_per_item(total, quantity):
#        s=int(total)
#        a=int(quantity)
#        try:
#            return s / a
#        except ZeroDivisionError as error:
#            return(error)


# def build_report(order):
#     return price_per_item(order["total"], order["quantity"])


# def main():
#     order = {"total": 600, "quantity": 0}
#     print(build_report(order))


# main()






# 9
# def line_total(price, quantity):
#     return price * quantity


# def cart_total(items):
#     total = 0
#     for index, item in enumerate(items):
#         price = item["price"]
#         quantity = item["quantity"]
#         total += line_total(price, quantity)
#     return total


# cart = [
#     {"name": "Mouse", "price": 100, "quantity": 2},
#     {"name": "Keyboard", "price": 250, "quantity": 1},
#     {"name": "Cable", "price": 30, "quantity": 3},
# ]
# print(cart_total(cart))





# 10
# from datetime import datetime
# def parse_date(text):
#     try:
#         return datetime.strptime(text, "%d.%m.%Y")
#     except ValueError:
#         raise ValueError(f"Invalid date format or value:{text}")

# text=input()
# print(parse_date(text).strftime("%Y-%m-%d"))





