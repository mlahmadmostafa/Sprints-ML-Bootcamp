import re

# input text
text = "here are some numbers: (123) 456-7890, 123-456-7890, (321)456-7890, and (555) 555-5555."

# regex for valid phone numbers in (xxx) xxx-xxxx format
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'

# regex to match any potential phone number
potential_numbers = r'(\(?\d{3}\)? ?\d{3}-?\d{4})'

# replace all invalid numbers with "invalid number"
validated_text = re.sub(potential_numbers, lambda match: match.group(0) if re.fullmatch(phone_pattern, match.group(0)) else "invalid number", text)

# print result
print(validated_text)
