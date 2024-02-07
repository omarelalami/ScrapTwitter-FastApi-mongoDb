import re

def clean_special_characters(text):
    """Cleans a string by handling various special characters and formatting issues."""

    # Normalize line endings
    text = re.sub(r'[\r\n\t]+', '\n', text)
    # Normalize commas and spaces around commas
    text = re.sub(r'\s*,\s*', ',', text)
    # Remove leading and trailing whitespace
    text = text.strip()
    # Remove backslashes
    text = re.sub(r'\\', '', text)
    # Remove # and other specified characters
    text = re.sub(r'[#\^&]', '', text)

    return text

def perform_data_cleaning(file_content):
    """Cleans the content of a file, handling lines and special characters."""

    # Clean each line using clean_special_characters function
    cleaned_lines = [clean_special_characters(line) for line in file_content.split('\n')]

    # Remove empty lines
    cleaned_lines = [line for line in cleaned_lines if line.strip()]

    # Join the cleaned lines back into a single string
    cleaned_file_content = '\n'.join(cleaned_lines)

    return cleaned_file_content

# Exemple d'utilisation
file_content = """Ceci est un exemple de texte
avec des sauts de ligne, des # et des caractères spéciaux ^&
"""

cleaned_file_content = perform_data_cleaning(file_content)

print(cleaned_file_content)
