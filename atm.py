class Atm:
    def __init__(self, number, pin):
        self.number = number
        self.pin = pin
    def balance(self):
        print("Your balance is 25 USD.")
    def withdraw(self, new):
        value = 25-new
        print("Your new balance is ", value)

atm1 = Atm(180, 169)
print(atm1.number)
atm1.balance()
atm1.withdraw(6)