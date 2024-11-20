
import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

COLS = 3
ROWS = 3

symbolCount = {
    "A" : 3,
    "B" : 4,
    "C" : 6,
    "D" : 5
}

symbolValues = {
    "A" : 8,
    "B" : 7,
    "C" : 6,
    "D" : 4
}


def deposit():
    while True :
        money = input("enter the amount you want to deposit:$")
        print("\n")
        try:
            money = int(money)
            if money > 0 :
                break
            else:
                print("please enter a positive number\n")
        except ValueError:
            print("please enter a number\n")

    return money



def getNumberOfLines():
    while True :
        lines = input("enter the number of lines between 1-" + str(MAX_LINES) + ":")
        print("\n")
        try:
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES :
                break
            else:
                print("please enter a  number between 1 and " + str(MAX_LINES)+"\n")
        except ValueError:
            print("please enter a number \n")

    return lines



def getBet():
    while True :
        bet = input("enter the amount you want to bet in each line \n must be betwwen "+ str(MIN_BET) + " and " + str(MAX_BET) + ":$")
        print("\n")
        try:
            bet = int(bet)
            if bet > MIN_BET and bet <= MAX_BET :
                break
            else:
                print("please enter a  number between " + str(MIN_BET) + " and " + str(MAX_BET) + "\n" )
        except ValueError:
            print("please enter a number \n")

    return bet
def getSlotMachineSpin(rows,cols,symbols):
    allSymbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        currentSymbol = allSymbols[:]
        for _ in range(rows):
            value = random.choice(allSymbols)
            currentSymbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns
a
def printSlotMachine(columns):
        for row in range(len(columns[0])):
            for i, col in enumerate(columns):
                if i != len(columns) - 1:
                    print(col[row], end=" | ")
                else:
                    print(col[row], end=" ")
            print()


def checkWining(columns, lines ,bet ,symbolValues) :
    winning = 0
    winningLines = []
    for line in range(lines) :
        symbol = columns[0][line]
        for column in columns :
            symbolCheck = column[line]
            if symbol != symbolCheck :
                break
        else:
            winning = bet* symbolValues[symbol]
            winningLines.append(line+1)
    return winning, winningLines

def game(balance):

    lines = getNumberOfLines()
    while True :
        bet = getBet()
        totalBet = (bet * lines)
        if totalBet <= balance :
            print("you have successfully deposited " + str(totalBet) +"\n")
            break
        else:
             print("u do not have $ " +str(totalBet)  + "in ur balance ")
    print(f"you are betting ${bet} on {lines} lines . ur total bet is :${totalBet} \n")

    slots= getSlotMachineSpin(ROWS, COLS, symbolCount)
    printSlotMachine(slots)

    winning,winningLines = checkWining(slots, lines, bet , symbolValues)
    if winning == 0 :
        print("you won nothing ")
        print(f"you lose the bet of ${totalBet}")
    else:
        print(f"you have won ${winning} ")
        print("in lines",*winningLines)
        print(f" your profit is ${winning - totalBet} ")
    return winning - totalBet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spin = input("press enter to spin ( q to quit). (d to deposite more)")
        if spin == "q" :
            break
        elif spin == "d" :
            print(f"ur balance is  ${balance}")
            newBalance = input("how much money do you want to add :$")
            newBalance = int(newBalance)
            balance = balance + newBalance
            print(f"ur new  balance is ${balance}")

        balance += game(balance)
        if balance == 0 :
            print("you have lost all ur money u need to deposit again")
            main()

    print(f"ur current balance is ${balance}")


main()