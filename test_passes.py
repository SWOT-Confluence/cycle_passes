"""Test extracting the right cycle and pass identifiers from pass number.

author: ntebaldi@umass.edu
date: 2022.02.10
"""

# Standard imports
import math

# Constants
TOTAL_PASSES = 585

def get_cycle_num(pass_no):
    """Get cycle number from pass numnber.
    
    Parameters
    ----------
    pass_no: number
        number of pass
    """
    
    return (math.floor((pass_no / TOTAL_PASSES)) + 1)

def get_pass_num(pass_no):
    """Get the pass number associated with the cycle.
    
    Parameters
    ----------
    pass_no: number
        number of pass
    """
    
    return pass_no % TOTAL_PASSES

def get_cycle_pass(pass_no):
    """Get cycle and pass identifiers from pass number.
    
    Parameters
    ----------
    pass_no: number
        number of pass
        
    Return
    ------
    tuple of cycle and pass number identifiers
    """
    
    c = get_cycle_num(pass_no)
    p = get_pass_num(pass_no)
    
    return (c,p)

if __name__ == "__main__":
    
    pass_no = 2
    c,p = get_cycle_pass(pass_no)
    print(c,p)