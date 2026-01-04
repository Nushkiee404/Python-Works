import random
 

secret_no = random.randint(1,50) 


attempt = 0

while True:
    guess = input("Enter your guess btw 1-50:")

    if not guess.isdigit():
        print("Invalid no.")
        continue
    
    guess = int(guess)
    attempt += 1

    if(guess<secret_no):
        print("Too less.Enter larger no.")
    elif(guess>secret_no):
        print("Too large.Enter a valid no")
    else:
        print(f"Congratulations!you guessed correct no. in {attempt} attempts")
        break
