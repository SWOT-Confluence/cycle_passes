"""Generates pass numbers associated with cycle and pass numbers.

author: ntebaldi@umass.edu
date: 2022.02.10
"""

# Standard imports
import glob
import json
from pathlib import Path

# Constants
CYCLES = 18
PASSES = 585

def generate_passes():
    """Generates pass numbers and associate with cycle and pass number ids.
    
    Returns
    -------
    dictionary of pass number keys and a list of cycle and pass identifiers
    """
     
    pass_dict = {}
    pass_no = 1
    for c in range(1, CYCLES + 1):
        for p in range(1, PASSES + 1):
            pass_dict[pass_no] = [c, p]
            pass_no += 1
        
    return pass_dict

def generate_cycle_passes():
    """Generate a dictionary of cycle_pass ids and pass numbers.

    Returns
    -------
    dictionary of cycle pass number ids and a value of pass number
    """
    
    cp_dict = {}
    pass_no = 1
    for c in range(1, CYCLES + 1):
        for p in range(1, PASSES + 1):
            cp_dict[f"{c}_{p}"] = pass_no
            pass_no += 1
        
    return cp_dict

def main(json_file_pn, json_file_cp):
    """Runs generate_passes and writes resulting data to JSON file.
    
    Parameters
    ----------
    json_file_pn: Path
        path to JSON file to write pass number data to.
    json_file_cp: Path
        path to JSON file to write cycle_pass identifiers to.
    """
    
    pass_dict = generate_passes()
    with open(json_file_pn, 'w') as jf:
        json.dump(pass_dict, jf, indent=2)
        
    cp_dict = generate_cycle_passes()
    with open(json_file_cp, 'w') as jf:
        json.dump(cp_dict, jf, indent=2)
        
if __name__ == "__main__":
    json_file_pn = Path("output pass JSON")
    json_file_cp = Path("output cycle and pass JSON")
    main(json_file_pn, json_file_cp)