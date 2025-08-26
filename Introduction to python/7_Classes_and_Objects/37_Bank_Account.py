class BankAccount:
  def __init__(self,first_name,last_name,account_id,account_type,pin,balance):
    self.first_name= first_name
    self.last_name=last_name
    self.account_id=account_id
    self.account_type=account_type
    self.pin=pin
    self.balance=balance
  def deposit(self,money):
    self.balance=money + self.balance
    return self.balance
  def withdraw(self,money):
    self.balance=self.balance - money
    return self.balance
  def display_balance(self):
    print(self.balance)
object1 = BankAccount('Deepika','Papitha',1234567,'Who knows',3456,78000.90)
print(object1.deposit(96))
object1.display_balance()
print(object1.withdraw(25))
object1.display_balance()