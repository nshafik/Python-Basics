
import random

def checkval(guess):
    try:
        if  int(guess) not in range(0,101) :
            return checkval(input("the number must be between 0 and 100! "))
        else:
            return int(guess)
    except:
        return checkval(input("Whoops! that's not a digit"))
    
    
Actual = random.randint(0,101)
print("Guess the number i have in mind, it's between 0 and 100")#Type Your Code Here - Replace None With Correct Function 

Guess= checkval(input("Type your Guess") )#Replace None Values with correct conditions or Booleans

guesses= [] #Make it an Empty List 
guesses.append(Guess)

while(True):
   # if  Guess not in range(0,101) :Guess=checkval(input("the number must be between 0 and 100! "))
                    
    if  Guess==Actual :
        print ("Wow, you've guessed Correctly this time") #Fix
        print('You have guessed it in {} times'.format(len(guesses)))
        break
    else:
        Guess=checkval(input('wrong, try another Guess'))
        guesses.append(Guess)
            
        if  abs(guesses[-1] - Actual) < abs(guesses[-2] - Actual) :
            print(' you are closer to target ')
        else:
            print(' you are far from the target ')
        
    
  
