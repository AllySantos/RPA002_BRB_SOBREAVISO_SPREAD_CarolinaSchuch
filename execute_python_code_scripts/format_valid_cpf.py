import sys
import re

# Remove dots, traces and any other non number character from cpf
def remove_non_numbers_characters(cpf):
    cpf_number = re.sub('[^0-9]', '', cpf)

    return cpf_number
    

# Get valid CPF's strings and format to correct pattern (000.000.000-00) 
def format_cpf(cpf):

    # Left only numbers in CPF
    cpf = remove_non_numbers_characters(cpf)

    formated_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    return formated_cpf


if __name__ == '__main__':

    # Get data from ElectroNeek
    input_cpf = sys.argv[1]

    formated_cpf = format_cpf(input_cpf)

    # Return formated cpf to ElectroNeek
    print(formated_cpf)