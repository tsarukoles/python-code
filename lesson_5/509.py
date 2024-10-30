# Test_509

def whatSquare(length, symbol, logic):
    if logic == True:
        for i in range(length):
            for j in range(length):
               print(symbol, end="\t")
            print()
    elif logic == False:
        for i in range(length):
            for j in range(length):
                if i == 0 or i == length - 1 or j == 0 or j == length - 1:
                    print(symbol, end="\t")
                else:
                    print(" ", end="\t")
            print()

whatSquare(5,"*", False)
print()
whatSquare(5,"*", True)