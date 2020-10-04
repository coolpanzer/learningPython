secret_word = "giraffe"
guess = ""
tries = 0
try_limit = 3
out_of_tries = False

while guess != secret_word and not(out_of_tries):
    if tries < try_limit:
        guess = input("Enter guess: ")
        tries += 1
    else:
        out_of_tries = True

if out_of_tries:
    print("You lose!")
else:
    print("You win!")