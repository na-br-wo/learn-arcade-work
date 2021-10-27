def to_celsius(p_fahrenheit=32):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters
    ----------
    p_fahrenheit : int
        The input temperature in Fahrenheit to convert to Celsius; default set
        to 32.
    freezingF : int
        The temperature at which Fahrenheit freezes.
    toCRatio : float
        Conversion factor to convert Fahrenheit to Celsius.
    C : float
        The temperature in Celsius that the function converts from Fahrenheit.
    """
    freezingF = 32
    toCRatio = 5/9
    C = toCRatio*(float(p_fahrenheit) - freezingF)
    return(round(C,2))
    
if __name__ == "__main__":
    C = to_celsius()
    print(round(C,2))
