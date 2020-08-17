def isAgain(answer):
    return answer == 1

def validateAnswer(answer):
   result = validateType(answer)
   if result == False:
       return print("Wrong Type!!!!!!!!!!!!!")
   return int(answer) == 0 or answer == 1

def validateType(answer):
    if(type(answer) != int):
        return False
    else:
        True

ascii_name = ''
MAXIMUM_LENGTH = 6
again = True
answer = 0        

while(again):    
    name = input("Enter your name: ")
    if (len(name) > MAXIMUM_LENGTH):
       print("Wow why such a long name?")
    else:
       print("That is the right amount of letters for any name!")
 
    for char in name:
            ascii_name += str(ord(char))
    print("Well either way whether your name is long or short" +
         "here is your name in ascii characters {}".format(ascii_name))
    
    answer = input("Would you like to enter a different name? 1 for yes 0 for no :")
    print(validateAnswer(answer))
    while(not(validateAnswer(answer))):
        answer = input("No seriously only a 1 or 0: yes or no")
    again = isAgain(answer)








