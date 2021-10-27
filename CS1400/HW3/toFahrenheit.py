#Celsius to Fahrenheit conversion by Nathan Wood

freezingF = 32 #constant variable at which water freezes in F
toFRatio = 9/5 #ratio for converting C to F

print('''Hello

This program will convert a temperature from Celsius to Fahrenheit.''')

C = int(input('Please enter a temperature in Celsius: ', )) #prompt user to enter a temp. in C

F = toFRatio*C + freezingF #The equation, changing the string input 'C' into an integer

print(round(F, 2), 'degrees Fahrenheit') #displaying the output
