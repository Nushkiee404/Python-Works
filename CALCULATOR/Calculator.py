keepGoing = True 

while keepGoing:
    expression = input("Give me an expression: ")
   
    numStr1, op, numStr2 = expression.split()
    num1 = float (numStr1)
    num2 = float (numStr2)

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print ("can't divide by 0,try again")
            continue
        else:
            result = num1 / num2
    else:
        print("Invalid operator, use +, -, *, or /.")
        continue
            
    print (numStr1,op,numStr2,'equals',result)

    tryAgain = input("Want to try again:")
            
    if tryAgain.lower() not in ['yes' ,'y']:
        keepGoing = False

        
        print("Thanks for playing")
        input("Hit any key to continue")