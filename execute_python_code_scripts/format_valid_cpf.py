import sys
import re

# Remove dots, traces and any other non number character from cpf
def remove_non_numbers_characters(cpf):
    cpf_number = re.sub('[^0-9]', '', cpf)

    return cpf_number
    

if __name__ == '__main__':

    # Get data from ElectroNeek
    input_cpf = sys.argv[1]

    formated_cpf = remove_non_numbers_characters(input_cpf)

    # Return formated cpf to ElectroNeek
    print(formated_cpf)