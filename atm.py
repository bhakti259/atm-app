# atm.py
class Atm:
    counter = 1

    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.serial_no = Atm.counter
        Atm.counter += 1

    def create_pin(self, new_pin):
        self.__pin = new_pin
        return "PIN set successfully!"

    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__balance += amount
            return f"Deposit successful! Balance: {self.__balance}"
        else:
            return "Invalid PIN!"

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return f"Withdrawal successful! Balance: {self.__balance}"
            else:
                return "Insufficient balance!"
        else:
            return "Invalid PIN!"

    def check_balance(self, pin):
        if pin == self.__pin:
            return f"Your balance is {self.__balance}"
        else:
            return "Invalid PIN!"
