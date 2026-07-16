import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # Load data from file
    if Path(database).exists():
        try:
            with open(database, "r") as fs:
                data = json.loads(fs.read())
        except Exception as err:
            print(f"An error has been occured : {err}")
    else:
        print("No such file exists")

    @staticmethod
    def __update():
        with open(Bank.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __gen(cls, gender):
        if gender == "Female":
            return random.choice("02468")
        else:
            return random.choice("13579")

    @classmethod
    def __accnogen(cls, gender):
        branch = "9891"
        accnum = "".join(random.choices(string.digits, k=9))
        last_digit = cls.__gen(gender)

        return branch + accnum + last_digit

    def accountcreate(self):
        try:
            info = {
                "name": input("Write your full name: "),
                "cnic": input("Write your CNIC (13 digits): "),
                "age": int(input("Write your age: ")),
                "gender": input("Write your gender (Male/Female): "),
                "balance": 0
            }

            # Validate CNIC
            while len(info["cnic"]) != 13 or not info["cnic"].isdigit():
                info["cnic"] = input("Invalid CNIC. Enter again: ")

            # Validate age
            if info["age"] < 18:
                print("Sorry! You cannot create a bank account.")
                return

            # Normalize gender
            if info["gender"].lower() in ("f", "female"):
                info["gender"] = "Female"
            elif info["gender"].lower() in ("m", "male"):
                info["gender"] = "Male"
            else:
                print("Invalid gender.")
                return

            # Generate account number
            info["accountnumber"] = Bank.__accnogen(info["gender"])

            # Save account
            Bank.data.append(info)
            Bank.__update()

            print("\nAccount created successfully.\n")

            for key, value in info.items():
                print(f"{key}: {value}")

            print("\nPlease note down your account number.")
        except Exception as err:
            print(f"An error has been occured : {err}")
    
    def deposit(self):
        try:
            cnic = input("Write your CNIC: ")
            accnum = input("Write your account number: ")

            userdata = [i for i in Bank.data if i["cnic"] == cnic and i["accountnumber"] == accnum]
            if bool(userdata) == False:
                print("No such data exist in the database")
            else:
                print(f"Your current balance is : {userdata[0]["balance"]}")
                deposit = int(input("Type the amount you deposit: "))
                if deposit > 0:
                    userdata[0]["balance"] += deposit
                    Bank.__update()
                    print("Amount deposit successfully")
                    print(f"Your new balance is : {userdata[0]["balance"]}")
        except Exception as err:
            print(f"An error has been occured : {err}")
    def withdraw(self):
        try:
            cnic = input("Write your CNIC: ")
            accnum = input("Write your account number: ")
            
            userdata = [i for i in Bank.data if i["cnic"] == cnic and i["accountnumber"] == accnum]
            if bool(userdata) == False:
                print("No such data exist in the database")
            else:
                print(f"Your current balance is : {userdata[0]["balance"]}")
                withdraw = int(input("Type the amount you withdraw: "))
                if withdraw > 0:
                    userdata[0]["balance"] -= withdraw
                    Bank.__update()
                    print("Amount withdraw successfully")
                    print(f"Your remaining balance is : {userdata[0]["balance"]}")
        except Exception as err:
            print(f"An error has been occured : {err}")
         

    def viewdetails(self):
        try:
            cnic = input("Write your CNIC: ")
            accnum = input("Write your account number: ")

            userdata = [i for i in Bank.data if i["cnic"] == cnic and i["accountnumber"] == accnum]

            if bool(userdata)  == False:
                print("No such data exist in the database")
            else:
                for i in userdata[0]:
                    print(f"{i}:{userdata[0][i]}")
        except Exception as err:
            print(f"An error has been occured : {err}")

    def deleteaccount(self):
        try:
            cnic = input("Write your CNIC: ")
            accnum = input("Write your account number: ")

            userdata = [i for i in Bank.data if i["cnic"] == cnic and i["accountnumber"] == accnum]

            if bool(userdata)  == False:
                print("No such data exist in the database")
            else:
                check = input("Are you sure to delete your account(Yes/No): ")
                if check.lower() in ('yes','y'):
                    index = Bank.data.index(userdata[0])
                    Bank.data.pop(index)
                    Bank.__update()
                    print("Your account deleted successfully")
        except Exception as err:
            print(f"An error has been occured : {err}")

    def updatedetails(self):
        try:
            cnic = input("Write your CNIC: ")
            accnum = input("Write your account number: ")

            userdata = [i for i in Bank.data if i["cnic"] == cnic and i["accountnumber"] == accnum]

            print("You cann't edit or update your bank account number, CNIC and age")

            update = {
                "name" : input("Write your new name: "),
                "gender": input("Write your new gender: ")
            }

            if update["gender"] == "":
                update["gender"] = userdata[0]["gender"]
                print("Your gender updated successfully")
                
            if update["gender"] == "":
                update["name"] = userdata[0]["name"] 
                print("Your name updated successfully")
            
            update["accountnumber"] = userdata[0]["accountnumber"]
            update["cnic"] = userdata[0]["cnic"]
            update["age"] = userdata[0]["age"]
            update["balance"] = userdata[0]["balance"]

            for i in update:
                if update[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = update[i]
            Bank.__update()
            print("Data updated successfully")
        except Exception as err:
            print(f"An error has been occured : {err}")






# ---------------- Main Program ----------------

user = Bank()

while True:

    print("\n========== JUTT BANK MANAGEMENT SYSTEM ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account")
    print("5. Update Account")
    print("6. Delete Account")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        user.accountcreate()
    elif choice == "2":
        user.deposit()
    elif choice =="3":
        user.withdraw()
    elif choice == "4":
        user.viewdetails()
    elif choice == "5":
        user.updatedetails()
    elif choice == "6":
        user.deleteaccount()

    elif choice == "7":
        print("Thank you for using our Bank System.")
        break

    else:
        print("This option is not implemented yet.")