from io import StringIO
import numpy as np

def cst_to_python(filename):
    """
    Convert data from a CST simulation file into Python-friendly arrays.

    Parameters:
    filename (str): The name of the CST simulation file to be processed.

    Returns:
    tuple: A tuple containing two elements:
        - parameters (numpy.ndarray): An array of parameter values extracted from the file.
        - arrays (list of numpy.ndarray): A list of NumPy arrays containing data from each data block in the file.
    
    Raises:
    Exception: If a parameter value cannot be found in a data block.

    This function reads a CST simulation file and extracts parameter values and data arrays from it. The file is assumed
    to contain multiple data blocks, each starting with a line like '#Parameters = {param_name=value}'. 
    The function identifies the parameter values, loads the data from each block, and returns them as NumPy arrays.

    Note: The CST simulation file should have a specific structure as described above for this function to work correctly.
    """
    data_blocks = load_data_blocks(filename)
    
    parameters = np.zeros((len(data_blocks)))
    arrays = []

    for i, data_block in enumerate(data_blocks):
        parameters[i] = identify_parameter_value(data_block)

    for i, data_block in enumerate(data_blocks):
        data = data_block_to_array(data_block)
        arrays.append(data)
    
    return parameters, arrays

def identify_parameter_value(data_block):
    """
    Extract a parameter value from a data block.

    Parameters:
    data_block (str): The data block containing parameter information.

    Returns:
    float: The extracted parameter value.

    This function extracts a parameter value from a data block. The parameter should be enclosed within curly braces 
    and have a format like {param_name=value}. The function parses and returns the numeric value.
    """
    start_index = data_block.find("{")
    end_index = data_block.find("}")
    if start_index != -1 and end_index != -1:
        extracted_value = data_block[start_index + 1:end_index]
    else:
        raise Exception("Could not find parameter value in data_block")

    start_index = extracted_value.find("=")
    extracted_value = extracted_value[start_index+1:]

    if extracted_value.find(";") != -1:
        extracted_value = extracted_value[:extracted_value.find(";")]

    return float(extracted_value)

def load_data_blocks(filename):
    """
    Load and split a CST simulation file into data blocks.

    Parameters:
    filename (str): The name of the CST simulation file to be processed.

    Returns:
    list of str: A list of data blocks extracted from the file.

    This function reads a CST simulation file and splits it into data blocks based on lines starting with 
    '#Parameters = '. The resulting list contains data blocks as separate strings.
    """
    with open(filename, 'r') as f:
        data_blocks = f.read().split('#Parameters = ')
    
    data_blocks = data_blocks[1:]  # Ignore the first (empty) element
    return data_blocks

def data_block_to_array(data_block):
    """
    Convert a data block into a NumPy array.

    Parameters:
    data_block (str): The data block to be converted.

    Returns:
    numpy.ndarray: A NumPy array containing the data from the data block.

    This function converts a data block (in string format) into a NumPy array. It assumes that the data block follows 
    a specific format with header lines to be skipped (at least 3 lines). The function reads and parses the data lines.
    """
    data = StringIO(data_block)
    return np.loadtxt(data, skiprows=3)
