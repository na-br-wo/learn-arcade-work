#Fahrenheit to Celsius conversion by Nathan Wood

freezingF = 32 #define the constant variable for freezing temp Fahrenheit
toCRatio = 5/9 #define ratio of F to C for conversion
#store this user input as variable (F)
#converts F to C with formula C = toCRatio(F - freezingF)
#displays results (which is C)
print('''Hello

This program will convert a temperature from Fahrenheit to Celsius.''')

F = input('Please enter a temperature in Fahrenheit: ', ) #prompt user to enter a temperature in F that will be converted to C.

C = toCRatio*(int(F) - freezingF) #The equation to convert F to C, changing user input from a string into an integer

print(round(C, 2), 'degrees Celsius') #Printing the answer in Celsius, rounding to 2 decimal places

