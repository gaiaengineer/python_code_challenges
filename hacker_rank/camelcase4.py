# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one

import sys
import re

def process_input_line(input_line):
    # Split the input line into operation, type, and name
    operation, data_type, variable_name = input_line.strip("()").split(";")
    
    # Check if the variable name contains spaces or is in camel case
    if " " in variable_name:
        variable_name_parts = variable_name.split()
    else:
        variable_name_parts = re.split("(?<=[a-z])(?=[A-Z])", variable_name)
    
    # Perform the specified operation on the variable name
    if operation == "S":
        # Operation 'S': Convert variable name to snake_case
        return " ".join([word.lower() for word in variable_name_parts])
    else:
        # Operation 'C' or 'M': Convert variable name to camelCase
        camel_case = variable_name_parts[0].lower() + "".join([word.capitalize() for word in variable_name_parts[1:]])
        
        # Determine the final result based on the type
        if data_type == "M":
            # Type 'M': Append parentheses for method names
            return camel_case + "()"
        elif data_type == "C":
            # Type 'C': Convert variable name to PascalCase
            return "".join([word.capitalize() for word in variable_name_parts])
        else:
            # Default case: Return camelCase for other types
            return camel_case

# Read input from standard input and replace carriage returns
complete_input = sys.stdin.read().replace("\r", "")

# Process each input line and store the results in a list
result_list = list(map(lambda input_line: process_input_line(input_line), complete_input.split("\n")))

# Print the final results, joined by newline characters
print("\n".join(result_list))