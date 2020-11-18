#Log for file 
#DATE         Change   
#11/17/20     Got rid of validateAnswer and validateType          
#             and type cast the args to get correct response
#
#

def isAgain(answer):
    return answer == 1


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


  
    if int(answer) == 0: 
        again = False
    elif int(answer) == 1:
        again = True
   
   
   









