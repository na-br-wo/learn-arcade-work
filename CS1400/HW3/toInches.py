#Centimeters to inches conversion by Nate Wood

toCm = 2.54 #conversion factor

print('''Hello

This program will convert a length from centimeters to inches.''')

CmLength = input('Please enter a length in centimeters: ', ) #prompt for user input

InLength = int(CmLength)/toCm

print(round(InLength, 2), 'inches') #displaying the results, rounded to 2 decimal places
