"""Crea una cuenta de banco que incluya:
Un único numero de cuenta, el balance de la cuenta, __int__, un deposito
donde meter dinero a la cuenta, un metodo para poder sacar dinero, 
y un metodo de balance de la cuenta, __str__
"""

class Client:
    def __init__(self, name, surname, pin):
        self.name = name
        self.surname = surname
        self.accounts = []
        self.pin = pin

    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_accounts(self):
        return ", ".join([str(account) for account in self.accounts])
    

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        """
        Cuentas={
        iban1: cuenta1,
        iban2: cuenta2,
        }
        """

    def add_account(self, account):
        self.accounts[account.account_number] = account
    def get_account(self):
        return self.accounts
    def get_account_by_number(self, account_number):
        return self.accounts[account_number]


class BankAccount:
    bank_name = "Uriel Bank"

    def __init__(self, account_number, client, currency="EUR"):
        self.account_number = account_number
        self.balance = 0
        self.currency = currency
        self.client = client
        self.client.accounts.append(self)

    def __str__(self):
        return f"Nº: {self.account_number}, Saldo: {self.get_balance()}, Propietario: {self.client}"

    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"Ingresaste {amount} {self.currency} en la cuenta {self.account_number}. Saldo actual: {self.balance} {self.currency}"

    def withdraw(self,amount):
        if amount > self.balance:
            return False
        self.balance = self.balance - amount
        return True
 
    def get_balance(self):
        return f"{round(self.balance, 2):.2f} {self.currency}"

    def get_bank_name(self):
        return self.bank_name
        
cliente1= Client("Uriel", "Gonzalez")

cuenta1= BankAccount("121212", cliente1)
cuenta2= BankAccount("161616", cliente1, "USD")

print(cuenta1.account_number, f"Tiene: {cuenta1.get_balance()}")
print(cuenta2.account_number, f"Tiene: {cuenta2.get_balance()}")

cuenta1.deposit(100)
print(cuenta1.withdraw(50))
print(cuenta2.withdraw(200))

print(cuenta1.account_number, f"Tiene: {cuenta1.get_balance()} y pertenece a {cuenta1.client}")
print(cuenta2.account_number, f"Tiene: {cuenta2.get_balance()} y pertenece a {cuenta2.client}")

print("Lista de cuentas del cliente: ", cliente1.get_accounts())