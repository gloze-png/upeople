import json

def read_dictionary_from_file(input_filename):
    """Reads a dictionary from a JSON file and returns it as a Python dictionary."""
    with open(input_filename, 'r') as file:
        data = json.load(file)
    return data

def invert_dictionary(original_dict):
    """Inverts the dictionary by making values keys and grouping original keys as values."""
    inverted_dict = {}
    for key, value in original_dict.items():
        if isinstance(value, str):  # Handling single values
            values = [value]
        else:  # Handling list values
            values = value
        
        for val in values:
            if val not in inverted_dict:
                inverted_dict[val] = []
            inverted_dict[val].append(key)
    return inverted_dict

def write_dictionary_to_file(output_filename, inverted_dict):
    """Writes the inverted dictionary to a JSON file."""
    with open(output_filename, 'w') as file:
        json.dump(inverted_dict, file, indent=4)

# Filenames
input_filename = "original_dict.json"
output_filename = "inverted_dict.json"

# Sample dictionary to store in a file
sample_dict = {
    "apple": "red",
    "banana": "yellow",
    "cherry": "red",
    "mango": "yellow",
    "grapes": ["black", "green"]
}

# Writing the sample dictionary to the input file
with open(input_filename, 'w') as file:
    json.dump(sample_dict, file, indent=4)

# Processing
original_dict = read_dictionary_from_file(input_filename)
inverted_dict = invert_dictionary(original_dict)
write_dictionary_to_file(output_filename, inverted_dict)

print(f"Inverted dictionary has been written to {output_filename}")
