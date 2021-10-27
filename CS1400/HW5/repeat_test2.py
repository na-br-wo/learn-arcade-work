'''
NAME:
    Repeat Joke Loop
    
DESCRIPTION:
    Tells the user a joke and keeps repeating it unless the user inputs "Quit."
    Is able to handle user input in different letter casing.
'''

#set the initial boolean value that will start the loop
stop_loop = False
#constructing the while(false) loop
while stop_loop == False:
    #takes an input from the user, asks the question
    joke_response = input('''Pete, Pete, and Repeat went out on the lake in a
boat. Pete and Pete fell out. Who is left? ''')
    #response necessary to break out of the loop
    if joke_response.upper() == 'QUIT':
        stop_loop = True #breaking the loop
        print('Goodbye, thanks for playing.') #goodbye message
    #simply repeat the loop if the natural "Repeat" response is given
    elif joke_response.upper() == 'REPEAT':
        stop_loop = False
    else:
        stop_loop = False
        #printing a new message if something other than the natural "Repeat"
        #response or "Quit" is given
        print('Nice try. Now, listen closely this time.')
