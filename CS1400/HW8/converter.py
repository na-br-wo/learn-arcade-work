import sys

mi_to_ft = 5280

def miles_to_feet(p_miles):
    feet = p_miles*mi_to_ft
    return(feet)

def proc_args(p_args):
    i = 0
    

# Main Section
if __name__ == "__main__":
    proc_args(sys.argv)

##    ft = miles_to_feet(26.2)
##    print("A marathon is",ft,"feet.")
