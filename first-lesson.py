def sixthline():
    answer = input('''Quiz time:
                      If I want to print 
                      the word cow,
                      what should i input?
                      1."cow"
                      2.cow
                      3.cow(1)
                      4.all of the above''')
    if answer == str(1):
        print('Correct. That is the end for this lesson.')
    else:
        print('You have gotten the answer wrong, try again.')
        sixthline()







def fifthline():
    c_b = input('To print a number, you can just put the number inbetween the parentheses (eg.print(1)')
    if c_b == "continue":
        sixthline()
    elif c_b == "back":
        fourthline()
    else:
        print('not valid input, please reinput')
        fifthline()






def fourthline():
    c_b = input('''To print a word, enter the word you want inbetween the parentheses in print() and quote it
                (eg.print("word"))''')
    if c_b == "continue":
        fifthline()
    elif c_b == "back":
        thirdline()
    else:
        print('not valid input, please reinput')
        fourthline()




def thirdline():
    c_b = input('Whatever you put between these the parentheses will be printed.(continue/back)')
    if c_b == "continue":
        fourthline()
    elif c_b == "back":
        secline()
    else:
        print('not valid input, please reinput')
        thirdline()


def secline():
    c_b = input('print() prints a word or number in a terminal.(continue/back)')
    if c_b == "continue":
        thirdline()
    elif c_b == "back":
        firstline()
    else:
        print('not valid input, please reinput')
        secline()




def firstline():
    c_b = input('Today we will learn about our first command, print() (input continue to continue)')
    if c_b == "continue":
        secline()
    else:
        print('not valid input, please reinput')
        firstline()
firstline()
