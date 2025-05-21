class BankAccount:
    def __init__(self, account_number, balance = 0):
      self.account_number = account_number
      self._balance = balance
      
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else :
            print("Deposit amount must be positive.")
    def widthdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
    
    def get_balance(self):
        return self._balance
    
    def _set_balance(self, new_balance):
        self.__balance = new_balance
        

class SavingAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied.")
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0, minimum_balance=500):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.get_balance() - amount < self.minimum_balance:
            print("Cannot withdraw. Minimum balance requirement not met.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            # use protected method to update balance
            self._set_balance(self.get_balance() - amount)
            print(f"Withdrew {amount}. New balance: {self.get_balance()}")
            