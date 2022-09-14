"""Generates pass numbers associated with cycle and pass numbers.

author: ntebaldi@umass.edu
date: 2022.02.10
"""

# Standard imports
import glob
import json
from pathlib import Path

def get_cycle_passes(pass_dir):
    """Get a dictionary of cycle and pass identifiers.
    
    Parameters
    ----------
    pass_dir: Path
        path to directory that contains cycle/pass shapefiles.
    
    Returns
    -------
    dictionary of cycle keys and list of pass numbers associated with cycle
    """
    
    # Create a dictionary of cycles and associated passes
    c_files = [Path(c_file).name for c_file in glob.glob(str(pass_dir / f"*Prior*NA*.shp"))]
    c_dict = {}
    for c_file in c_files:
        key = int(c_file.split('_')[5])
        if key in c_dict.keys():
            c_dict[key].append(int(c_file.split('_')[6]))
        else:
            c_dict[key] = [int(c_file.split('_')[6])]
            
    # Sort pass identifiers for each cycle
    for value in c_dict.values(): value.sort()
    
    return c_dict
    

def generate_passes(pass_dir):
    """Generates pass numbers and associate with cycle and pass number ids.
    
    Parameters
    ----------
    pass_dir: Path
        path to directory that contains cycle/pass shapefiles.
    
    Returns
    -------
    dictionary of pass number keys and a list of cycle and pass identifiers
    """
    
    c_dict = get_cycle_passes(pass_dir)
    cycles = list(c_dict.keys())
    cycles.sort()
    
    pass_dict = {}
    pass_no = 1
    for c in cycles:
        for p in c_dict[c]:
            pass_dict[pass_no] = [c, p]
            pass_no += 1
        
    return pass_dict

def generate_cycle_passes(pass_dir):
    """Generate a dictionary of cycle_pass ids and pass numbers.
    
    Parameters
    ----------
    pass_dir: Path
        path to directory that contains cycle/pass shapefiles.
    
    Returns
    -------
    dictionary of cycle pass number ids and a value of pass number
    """
    
    c_dict = get_cycle_passes(pass_dir)
    cycles = list(c_dict.keys())
    cycles.sort()
    
    cp_dict = {}
    pass_no = 1
    for c in cycles:
        for p in c_dict[c]:
            cp_dict[f"{c}_{p}"] = pass_no
            pass_no += 1
        
    return cp_dict
    
    
def main(pass_dir, json_file_pn, json_file_cp):
    """Runs generate_passes and writes resulting data to JSON file.
    
    Parameters
    ----------
    pass_dir: Path
        path to directory that contains cycle/pass shapefiles.
    json_file_pn: Path
        path to JSON file to write pass number data to.
    json_file_cp: Path
        path to JSON file to write cycle_pass identifiers to.
    """
    
    pass_dict = generate_passes(pass_dir)
    with open(json_file_pn, 'w') as jf:
        json.dump(pass_dict, jf, indent=2)
        
    cp_dict = generate_cycle_passes(pass_dir)
    with open(json_file_cp, 'w') as jf:
        json.dump(cp_dict, jf, indent=2)
        
if __name__ == "__main__":
    pass_dir = Path("swot shapefiles")
    json_file_pn = Path("output pass JSON")
    json_file_cp = Path("output cycle and pass JSON")
    main(pass_dir, json_file_pn, json_file_cp)