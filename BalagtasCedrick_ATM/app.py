BalagtasIsActive = False
BalagtasATM = True
BalagtasBalance = 1000000

def BalagtasLogin():
    BalagtasMain()
    global BalagtasATM
    global BalagtasIsActive
    print("---------W E L C O M E---------")
    print("")
    print("         1. Log In")
    print("         2. Exit")
    print("")
    print("-------------------------------")
    BalagtasInput = input("Enter : ")
    if BalagtasInput == "1":
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("    Logged In Successfully  ")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        BalagtasIsActive = True
    elif BalagtasInput == "2":
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("      Program Terminated    ")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        BalagtasATM = False
    else:
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("  You can only type 1 or 2 ;D")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

def BalagtasDashboard():
    BalagtasMain()
    global BalagtasBalance
    global BalagtasIsActive
    print("------------M E N U------------")
    print("")
    print("         1. Balance")
    print("         2. Deposit")
    print("         3. Withdraw")
    print("         4. Logout")
    print("")
    print("-------------------------------")
    BalagtasInput = input("Enter : ")
    if BalagtasInput == "1":
        while True:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print(" Balance: ₱{:,.2f}".format(BalagtasBalance))
            BalagtasReturnInput = input("\n      Return? [y]: ")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            if BalagtasReturnInput == "y" or BalagtasReturnInput == "Y":
                return BalagtasDashboard()
            else:
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                print("      Type Y to return :D   ")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    elif BalagtasInput == "2":
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("            DEPOSIT         ")
        try:
            BalagtasDepositInput = float(input(" Deposit Amount : "))
            if BalagtasDepositInput >= 100 and BalagtasDepositInput <= 50000:
                print("")
                print("          Successful !")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                BalagtasBalance = BalagtasBalance + BalagtasDepositInput
            elif BalagtasDepositInput > 50000:
                print("")
                print("            Failed !")
                print("       Maximum of ₱50,000")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            else:
                print("")
                print("            Failed !")
                print("         Minimum of ₱100")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        except ValueError:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("  Try typing a number instead! ")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            return

    elif BalagtasInput == "3":
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("           WITHDRAW         ")
        try:
            BalagtasWithdrawInput = float(input(" Withdraw Amount : "))
            if BalagtasWithdrawInput <= 20000 and BalagtasWithdrawInput >= 1000:
                print("")
                print("          Successful !")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                BalagtasBalance = BalagtasBalance - BalagtasWithdrawInput
            elif BalagtasWithdrawInput < 1000:
                print("")
                print("            Failed !")
                print("        Minimum of ₱1,000")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            else:
                print("")
                print("            Failed !")
                print("     Daily Limit of ₱20,000")
                print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        except ValueError:
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            print("  Try typing a number instead! ")
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
            return

    elif BalagtasInput == "4":
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("    Logged Out Successfully ")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        BalagtasIsActive = False
    else:
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("  You can only type (1-4)  :P")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")


def BalagtasMain():
    print("===============================")
    print("            A  T  M            ")
    print("===============================")

while BalagtasATM == True:

    while BalagtasIsActive == False and BalagtasATM == True:
        BalagtasLogin()

        while BalagtasIsActive == True:
            BalagtasDashboard()







