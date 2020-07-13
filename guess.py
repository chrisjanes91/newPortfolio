numbers = [4, 6, 9]

while True:
	guess = input("Guess a number between 1 and 10, or type q to quit: ")
	guess = int(guess)
	if guess == "q":
		break
	if guess in numbers:
		print("Congratulations, you are correct!")
		break
	else:
		print("Incorrect! Guess again!")


    