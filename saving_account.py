class BankAccount:
    def __init__(self, owner, account_number, account_name, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.account_name = account_name
        self.set_balance(balance)

    def get_account_number(self):
        return self.account_number

    def get_account_name(self):
        return self.account_name

    def get_balance(self):
        return self.balance

    def display(self):
        print(f"{self.get_account_number()} - {self.get_account_name()} - {self.get_balance()}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def set_balance(self, new_balance):
        if new_balance > 0:
            self.balance = new_balance
        else:
            print("Không hợp lệ")


class SavingAccount(BankAccount):
    def __init__(self, monthly_interest_rate, *args, **kwarg):
        self.monthly_interest_rate = monthly_interest_rate
        super().__init__(*args, **kwarg)

    def calculate_interest(self):
        return self.balance * self.monthly_interest_rate


class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_info(self):
        print(f"{self.get_name()} - {self.get_date_of_birth()} - {self.get_email()} - {self.get_phone()}")


if __name__ == "__main__":
    my_account = Customer("Hà", 12000000, "ha@gmail.com", "0900000999")
    my_account.get_info()
    bank_account = BankAccount(my_account, 123, 'Vip account', 100000000)
    bank_account.display()
    bank_account.get_balance()
