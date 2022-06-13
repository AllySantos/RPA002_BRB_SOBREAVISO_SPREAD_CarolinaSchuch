import sys

# Get valid CPF's strings and format to correct pattern (000.000.000-00) 
def format_cpf(cpf):

    formated_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'

    return formated_cpf


if __name__ == '__main__':

    # Get data from ElectroNeek
    input_cpf = sys.argv[1]

    formated_cpf = format_cpf(input_cpf)

    # Return formated cpf to ElectroNeek
    print(formated_cpf)