#Inches to centimeters conversion by Nathan Wood

toCm = 2.54 #Conversion factor that will convert inches to centimeters

print('''Hello

This program will convert a length from inches to centimeters.''')

InLength = input('Please enter a length in inches: ', ) #prompt the user to input length

CmLength = toCm*(int(InLength)) #equation to convert inches to cm, chaging the user entry from string to integer

print(round(CmLength, 2), 'cm') #displaying the results
