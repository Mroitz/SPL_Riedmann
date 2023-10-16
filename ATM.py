working = True
balance = 0;

while working:
    selection = int(input("Einzaheln: 1\n" "Abheben: 2\n" "Kontostand: 3\n" "Beenden: 4\n"))

    if selection == 1:
        deposit = int(input("Enter amount: \n"))
        balance += deposit
        print("you succesfully added " + str(deposit) + " to your account \n")
        print("Balance: " + str(balance) + "\n")

    if selection == 2:
        withdraw = int(input("Enter amount: \n"))
        balance -= withdraw
        print("you succesfully withdrew " + str(withdraw) + " from your account \n")
        print("Balance: " + str(balance) + "\n")
        if withdraw > balance:
            print("zu wenig Geld")

    if selection == 3:
        print("Balance: " + str(balance) + "\n")

    if selection == 4:
        working = False
