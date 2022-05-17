import sys
import re


def remove_characters(cpf: str) -> str:
    # Replace any non-number character for ''
    return re.sub('[^0-9]', '', cpf)


def validate_length(cpf: str) -> bool:
    if len(cpf) == 11:
        return True
    return False


def validate_digits(cpf: str) -> bool:
    # Verify if it has all equal numbers
    first_number = cpf[0]

    if cpf == (first_number * 11):
        return False

    # Get the first 9 digits and validate the 9th one
    slice_cpf = cpf[0:9]
    digit = cpf[9]
    validate_first_digit = calculate_digit(slice_cpf, digit)

    # Get the first 10 digits and validate the last one
    slice_cpf = cpf[0:10]
    digit = cpf[10]
    validate_second_digit = calculate_digit(slice_cpf, digit)

    # If both are valid return true
    return validate_first_digit and validate_second_digit


# Return if the given digit it's valid
def calculate_digit(slice_cpf, digit):
    index = len(slice_cpf) + 1

    sum = 0
    for cpf_digit in slice_cpf:
        sum += int(cpf_digit) * index
        index -= 1

    mod_sum = sum % 11

    calc_digit = 11 - mod_sum

    if calc_digit > 9:
        calc_digit = 0

    # Return true if the calculate digit it's equal to given digit
    if calc_digit == int(digit):
        return True

    return False


if __name__ == '__main__':
    # Get data from Electrokeev
    cpf = sys.argv[1]
   
    # Left only numbers
    cpf = remove_characters(cpf)

    # Verify if cpf's length and digits are correct
    isCpfValid = validate_length(cpf) and validate_digits(cpf)

    # Return data to ElectroNeek
    print(isCpfValid)