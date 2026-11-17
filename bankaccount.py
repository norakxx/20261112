"""Crea una cuenta de banco que incluya:
Un único numero de cuenta, el balance de la cuenta, __int__, un deposito
donde meter dinero a la cuenta, un metodo para poder sacar dinero, 
y un metodo de balance de la cuenta, __str__
"""

class Client:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f"{self.name} {self.surname}"

    def get_accounts(self):
        return ", ".join([str(account) for account in self.accounts])

class bankaccount:
    bank_name = "Bank of Uriel"

    def __init__(self, account_number, client_name, currency="EUR"):
        self.account_number = account_number
        #Guardamos el dinero en integer
        self.balance = 0
        self.currency = currency
        self.client_name = client_name
        self.client_name.accounts.append(self)

    def __str__(self):
        return f"Cuenta: {self.account_number}, Saldo: {self.balance} {self.currency}, Propietario: {self.client_name}"

    def deposit(self, amount):
        self.balance= self.balance + amount
        return f"Ingresaste {amount}€ en la cuenta {self.account_number}, ahora tienes {self.balance}€" 

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance= self.balance - amount
        return True
    
    def get_blalance(self):
        return f"{round(self.balance, 2):.2f} {self.currency}"
    
    def get_bank_name(self):
        return f"{self.bank_name}"
        
cliente1= Client("Uriel", "Gonzalez")

cuenta1= bankaccount("121212", cliente1.name)
cuenta2= bankaccount("161616", cliente1.name,"USD")

print(cuenta1.account_number, f"Tiene: {cuenta1.get_balance()}")
print(cuenta2.account_number, f"Tiene: {cuenta2.get_balance()}")

cuenta1.deposit(100)
print(cuenta1.withdraw(50))
print(cuenta2.withdraw(200))

print(cuenta1.account_number, f"Tiene: {cuenta1.get_balance()} y pertenece a {cuenta1.client_name}")
print(cuenta2.account_number, f"Tiene: {cuenta2.get_balance()} y pertenece a {cuenta2.client_name}")

print("Lista de cuentas del cliente: ", cliente1.get_accounts())