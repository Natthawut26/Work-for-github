print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

answer = input('2+2=? \n ')
if answer.lower() == '4':
    print("Correct")
    score += 1
else:
    print('Wrong')
 
answer = input('50+30=? \n ')
if answer.lower() == '80':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('3+2*5=? \n ')
if answer.lower() == '13':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('8-5*2? \n ')
if answer.lower() == '-2':
    print("Correct")
    score += 1
else:
    print('Wrong')

answer = input('(100-50)+2*2? \n ')
if answer.lower() == '54':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")
