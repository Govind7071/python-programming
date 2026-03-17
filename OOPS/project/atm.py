class atm :
    def __init__(self):
        print("Welcome to ATM System")
        self.pin = ''
        self.balance = 10000
        self.pin = input("enter the pin")
        self.menu()


    def menu(self):
            data = int(input("Select a option \n 1. Check Balance\n 2. Deposit Money\n 3. Withdraw Money \n 4. Transfer Money \n 5.Change PIN \n 6. Exit\n"))

            match data :
                 case 1 : self.check_balance()
                 case 2 : self.Deposit_Money()
                 case 3 : self.Withdraw_Money()
                 case 4 : self.Transfer_Money()
                 case 5 : self.change_pin()
                 case 6 : self.Exit()
                 case _ : 
                    print("Invalid button press,try again")
                    self.menu()


              


    def check_balance(self):

         print(f"Your balance is {self.balance}")

         return self.menu()


    def Deposit_Money(self):
         deposit = int(input("Enter the balance to be deposted"))
         self.balance+=deposit

         self.check_balance()
    

    def Withdraw_Money(self):
        withdraw = int(input("Enter the amount : "))
        if withdraw > self.balance :
             print("Invalid transaction")
             self.menu()
             return 

        
        self.balance -= withdraw
        print("Withdrawl successful")
        self.check_balance()


    def Transfer_Money(self):
        acc = int(input("Enter the reciever account number :"))
        amount = int(input("Enter the fund to transfer :"))

        if amount > self.balance :
             print("Cannot complete transaction")
             self.menu()
             return 
        self.balance -= amount
        print("fund transfer successfully")
        self.check_balance()


    def change_pin(self) :
         verify_pin = (input("Enter the existing pin "))

         if verify_pin == self.pin :
             new_pin = input("Enter new pin :")
             self.pin = new_pin
             print("Pin changed successfully")
         else:     
            print("Wrong pin entered")
         self.menu()
        
    def Exit(self):
         print("Thank You for connecting with us\n Visit again")
         exit()



c1 = atm()