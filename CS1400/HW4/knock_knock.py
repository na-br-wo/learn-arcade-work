#Knock Knock joke program for CS1400 by Nathan Wood

'''
NAME:
    Knock-Knock Joke
DESCRIPTION:
    The module will ask the user if they want to hear a knock-knock joke. If
    they do, it will tell them a joke all the way through until the punchline.
    It will then say goodbye. If they don't want to hear the joke, it will tell
    them goodbye. It will tell them to try again if they enter incorrect
    responses to the knock-knock prompts.
'''

#Ask user for input: "Would you like to hear a knock-knock joke?
answer = input('Would you like to hear a knock-knock joke? ')

if answer.upper() == 'NO': #using .upper() to accept any case
    '''
    NAME:
        Negative Response

    DESCRIPTION:
        If the user says they DO NOT want to hear a knock-knock joke, then this
        module says "Goodbye."
    '''
    print('Sorry to hear that. Goodbye.')

elif answer.upper() == 'YES': #using .upper() to accept any case
    '''
    NAME:
        Positive Response

    DESCRIPTION:
        If the user says they DO want to hear a knock-knock joke, then this
        module tells them a joke. It starts the joke and asks for an input.
        
    '''
    response = input('Knock, knock. ')

    if response.upper() == "WHO'S THERE?": #using .upper() to accept any case
        '''
        NAME:
            First Question

        DESCRIPTION:
            If the user responds in knock-knock joke structure, this module
            continues the joke and asks for a new input.
        '''
        response_2 = input('Boo ')

        if response_2.upper() == "BOO, WHO": #using .upper() to accept any case
            '''
            NAME:
                Punchline

            DESCRIPTION:
                If the user responds correctly to the previous prompt, this
                module delivers the punchline. It then thanks the user for
                playing and says "Goodbye." This module imports the time
                module to let the computer pause before delivering its goodbye.
            '''
            print("Don't need to cry about it.")
            import time
            time.sleep(1) #Import time and have computer pause for a bit
            print("Thank you for playing. Goodbye")

        else:
            '''
            NAME:
                Try-Again prompt -- "Boo, who"

            DESCRIPTION:
                If the user does not respond "Boo, who" to the First Question
                module's input prompt, this module tells the user to try again.
            '''
            #started a newline with the print so it's not too long a string
            print('Are you sure you know how knock-knock jokes work?'
                  ' Try again.'
                  )

    else:
        '''
        NAME:
            Try-Again prompt -- "Who's there?"

        DESCRIPTION:
            If the user does not respond "Who's there?" to the Positive
            Response module's input prompt, this module tells the user to try
            again.
        '''
        print('Are you sure you know how knock-knock jokes work? Try again.')
        
                    

        
        
        


        

    



    
