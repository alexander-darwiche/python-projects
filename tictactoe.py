def print_board():
    count = 0
    for i in range(0,5):
        if i % 2 == 1:
            string = 5*'-'
        else:
            string = str(answer[(count*3)]) + '|' + str(answer[(count*3)+1]) + '|' + str(answer[(count*3)+2])
            count += 1
        print(string)


def prompt_user_x():
    input_value = input("Which square would you like to add an x? (1-9)")
    if input_value not in answer:
        print("Try Again")
        prompt_user_x()
    else:
        answer[input_value] = 'x'


def prompt_user_o():
    input_value = input("Which square would you like to add an o? (1-9)")
    if input_value not in answer:
        print("Try Again")
        prompt_user_o()
    else:
        answer[input_value] = 'o'



def check_for_win(gameIsPlaying):
    if (answer[0] == answer[1] == answer[2]) or (answer[0] == answer[3] == answer[6]):
        gameIsPlaying = False
    elif answer[6] == answer[7] == answer[8] or answer[2] == answer[5] == answer[8]:
        gameIsPlaying = False
    elif answer[0] == answer[4] == answer[8] or answer[2] == answer[4] == answer[6]:
        gameIsPlaying = False
    return(gameIsPlaying)



# Initilization phase
answer = [i for i in range(0,9)]
x_or_o = 0
gameIsPlaying = True

while gameIsPlaying:
    print_board()
    if (x_or_o % 2 == 0):
        prompt_user_x()
        x_or_o += 1
    else:
        prompt_user_o()
        x_or_o += 1
    gameIsPlaying = check_for_win(gameIsPlaying)

print_board()
if x_or_o % 2 == 0:
    print("Player 1 (X) is the winner!")
else:
    print("Player 2 (O) is the winner!")
