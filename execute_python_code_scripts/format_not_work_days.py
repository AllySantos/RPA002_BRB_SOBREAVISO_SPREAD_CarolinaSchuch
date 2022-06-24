import sys
import re


# Remove any character (except commas)
def remove_characters(text: str) -> str:

    # Replace any non-number character for ''
    return re.sub('(?i)([.]|[a-zA-Z])', '', text)

# Remove remaining commas and white spaces
def remove_commas(text: str) -> str:
    # Remove white spaces
    text = re.sub(' ', '', text)

    # Remove more than one comma and replace by one (,,,,,,,,,,,, = ,)
    text = re.sub('(,)+', ',', text)


    text_length = len(text)
    last_character = text[text_length - 1]

    # If remain a comma at the end of the text, remove it    
    if last_character == ',':
        text = text[:-1]

    return text



if __name__ == '__main__':
    # Get data from ElectroNeek
    plain_text = sys.argv[1]

    new_text = remove_characters(plain_text)  # text with just numbers and commas

    new_text = remove_commas(new_text)  # text with no remaining commas and whitespace

    # Return new_text to ElectroNeek
    print(new_text)
