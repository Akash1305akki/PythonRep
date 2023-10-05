class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute
        print("Initially:-\nAccount  Number: " + account_number, "\nBalance: " + str(balance))

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self._account_number


# Creating an object of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing the public methods of the class
account.deposit(500)
account.withdraw(200)

# Accessing the public getters to retrieve private and protected attributes
print("After Transaction:-")
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())

print("--------------------------------------------")


class GetProtectedVar(BankAccount):
    def variables(self):
        pass


obj = GetProtectedVar("12453267", 300)
print(obj._account_number)
# print(obj.__balance)

print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")

