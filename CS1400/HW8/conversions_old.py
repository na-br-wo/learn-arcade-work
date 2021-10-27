# Command-Line Argument Testing with various conversion factors

import sys

def to_celsius(p_fahrenheit=32):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters
    ----------
    p_fahrenheit : int
        The input temp. in Fahrenheit to convert to Celsius; default set to 32.
    freezingF : int
        The constant at which Fahrenheit freezes; used in conversion equation.
    toCRatio : float
        Conversion factor to convert Fahrenheit to Celsius.
    C : float
        The temp. the function converts from Fahrenheit to Celsius.

    Notes
    -----
    Returns a value rounded to 2 decimal places, this rounding chan be changed
    or omitted if desired.
    """
    freezingF = 32
    toCRatio = 5/9
    C = toCRatio*(float(p_fahrenheit) - freezingF)
    return(round(C,2))

def to_fahrenheit(p_celsius=0):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters
    ----------
    p_celsius : int
        The input temp. in Celius to convert to Fahrenheit; default set to 0.
    freezingF : int
        The constant at which Fahrenheit freezes; used in conversion equation.
    toFRatio : float
        Conversion factor to convert Celsius to Fahrenheit.
    F : float
        The resulting temp. conversion.

    Notes
    -----
    Returns a value rounded to 2 decimal places, this rounding chan be changed
    or omitted if desired.
    """
    freezingF = 32
    toFRatio = 9/5
    F = toFRatio*p_celsius + freezingF
    return(round(F,2))

def to_inches(p_cm=10):
    """
    Converts a length from centimeters to inches.

    Paramters
    ---------
    p_cm : int
        Input length in centimeters to convert to inches; default set to 10.
    to_in : float
        Conversion factor, used to divide user input.
    in_len : float
        The resulting length conversion.

    Notes
    -----
    Returns a value rounded to 2 decimal places, this rounding chan be changed
    or omitted if desired.
    """
    to_in = 2.54
    in_len = float(p_cm)/to_in
    return(round(in_len,2))

def to_cm(p_in=6):
    """
    Converts a length from inches to centimeters.

    Paramters
    ---------
    p_in : int
        Input length in inches to convert to centimeters; default set to 6.
    to_cm : float
        Conversion factor, used to multiply user input.
    cm_len : float
        The resulting length conversion.
    
    Notes
    -----
    Returns a value rounded to 2 decimal places, this rounding chan be changed
    or omitted if desired.
    """
    to_cm = 2.54
    cm_len = float(p_in)*to_cm
    return(round(cm_len,2))

## Print args function will list options for conversion factors.
def print_args():
    """
    Prints a list of options for controlling the conversion module.
    """
    print("""
         Conversions
         -----------
         Here is a list of conversions. To convert a value,
         type the letter that corresponds with the conversion
         you wish to attempt, followed by the number you wish
         to convert.

         (s) -- converts number from fahrenheit to celsius
         (f) -- converts number from celsius to fahrenheit
         (c) -- converts number from inches to centimeters
         (i) -- converts number from centimeters to inches
         """
        )

def no_param_mode():
    print('Which conversion utility would you like to run?')

def process_args(p_args):
    i=1
    if len(p_args) < 2:
        no_param_mode()
    else:
        for arg in p_args:
            ##print(i,arg,'p_arg[i+1]',p_args[i+1])
            if arg == 's':
                try:
                    c_temp=to_celsius(float(p_args[i+1]))
                    print(p_args[1],'degrees fahrenheit converts to:',c_temp,
                          'degrees fahrenheit.')
                except ValueError:
                    print('Can only convert numeric values.')
            if arg == 'f':
                try:
                    f_temp=to_fahrenheit(float(p_args[i+1]))
                    print(arg,'degrees celsius converts to:',f_temp,
                          'degrees celsius.')
                except ValueError:
                    print('Can only convert numeric values.')
            if arg == 'c':
                try:
                    c_len=to_cm(float(p_args[i+1]))
                    print(arg,'inches converts to:',c_len,'centimeters.')
                except ValueError:
                    print('Can only convert numeric vaues.')
            if arg == 'i':
                try:
                    in_len=to_inches(float(p_args[i+1]))
                    print(arg,'centimeters converts to:',in_len,'inches.')
                except ValueError:
                    print('Can only convert numeric values.')
    i = i+1
                

if __name__ == "__main__":
    process_args(sys.argv)


    
